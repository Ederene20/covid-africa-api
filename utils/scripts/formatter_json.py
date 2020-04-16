
def formatter(data):
    """
    Format the data returned by the scraper in usable format
    """

    # we delete the first and the last element of the list
    del data[0]
    data.pop()

    data_stats = {}

    country_stats = {}

    for element in data:

        element = element.split()
        element.pop()  # we delete the last element of the list which is a reference

        # some country have very long names so we extract the first strings
        country = element[:-3]
        # which represent the name of the country

        country = " ".join(country)
        # each element has a structure like this : ["countryname","number of case","number of death","number of recovered"]
        data_stats[country] = {
            "case_number": element[-3].replace(',', ''),
            "case_death": element[-2],
            "case_recovered": element[-1]
        }
    return data_stats
