import mechanicalsoup


def get_owner_name_from_address(address):

    browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup')
    browser.open("https://www.stlouis-mo.gov/data/address-search/index.cfm")

    # Fill-in the search form
    browser.select_form(nr=1)
    browser["streetAddress"] = address
    browser.submit_selected()
    property_owners = browser.page.find(text='Owner name').findNext('td').text
    print(property_owners)
    return property_owners


def current_test():
    get_owner_name_from_address('5100 DRESDEN AV')
    get_owner_name_from_address('4095 WILMINGTON AVE')


def main():
    data_file_location = "data/city voters non-apts - CountyWide_VotersList_08202020_.csv" # noQA
    output_file_location = "data/output.csv"

    street_number_idx = 3
    street_name_idx = 5
    street_type_idx = 6
    output_file = ''

    with open(data_file_location) as data_file:
        for line in data_file:
            output_file += line[:-1]
            print(line)
            fields = line.split(',')
            assembled_address = ''
            assembled_address += fields[street_number_idx] + ' '
            assembled_address += fields[street_name_idx] + ' '
            assembled_address += fields[street_type_idx]
            print(assembled_address)
            property_owners = get_owner_name_from_address(assembled_address)
            output_file += property_owners + '\n'
            # print(output_file)

    with open(output_file_location, 'w') as o:
        o.write(output_file)


if __name__ == '__main__':
    main()
