# The Census classifies cities and other municipalities as "places". 
# You will find place codes using the Geographic Codes Lookup at the Missouri Census Data Center: https://census.missouri.edu/geocodes/

# The variables to request are place names and total population.

import requests 

# This is the structure of the  intal point of access for the census database api
# Here you will need to create an appropriate string values to retrieve data for:
# year (2010) from dataset (Summary File 1 of the Decennial Census), base_url
# (for this prticular case of API usage in the case of US censu their is strict from to Build base URL)
HOST = "https://api.census.gov/data"
year = "2010"
dataset = "dec/sf1"
base_url = "/".join([HOST, year, dataset])

# Build dictionary of predicates, here the name and total population varaible have been passed to get_vars
get_vars = ["NAME", "P001001"] # <- total population
predicates = {}
predicates["get"] = ",".join(get_vars)

# Here you will use GEOID of the place geogrpahic nature.
# Using the Missouri Census Data Center, find 
# (1) the two digit state code for Pennsylvania and 
# (2) the five digit place codes for the cities of Philadelphia and Pittsburgh

# This is the site to find the GEOID (https://census.missouri.edu/geocodes/?state=00)
# Set the "for" predicate to request the two place codes you found for Philadelphia and Pittsburgh, separated by a comma
predicates["for"] = "place:60000,61000"

# The state geoid is often a long value only use the two digits after US
# Set the "in" predicate to request the state code you found for Pennsylvania
predicates["in"] = "state:42"


# Execute the request
r = requests.get(base_url, params=predicates)

# Show the response text
print(r.text)
