import requests 
import pandas as pd

# This is the structure of the  intal point of access for the census database api
# Here you will need to create an appropriate string values to retrieve data for:
# year (2010) from dataset (Summary File 1 of the Decennial Census), base_url
# (for this prticular case of API usage in the case of US censu their is strict from to Build base URL)
HOST = "https://api.census.gov/data"
year = "2010"
dataset = "dec/sf1"
base_url = "/".join([HOST, year, dataset])

# Construct get_vars, which is the list of Census variables to request, 
# with the following variable names: 
# "NAME"(well be fit the geogrpahicy level in predicates), 
# "P013001" (median age),
# "P037001" (average family size)
# Specify Census variables and other predicates
# predicates here is the output the APi with provide,
# "get" strucues the requests.
# "for" specficy the geographic level
get_vars = ["NAME", "P013001", "P037001"]
predicates = {}
predicates["get"] = ",".join(get_vars)

# To begin we will Build dictionary of predicates and execute the request
# Set the "for" key in the predicates dict to return all Congressional districts.
# We can do so by Spelling out congressional district in full, and the place(:*) for all within.
predicates["for"] = "congressional district:*"
# We will set the "in" key in the predicates dict to only return:
# Geographies in the state of Pennsylvania, which use the geoid 42
predicates["in"] = "state:42"
r = requests.get(base_url, params=predicates)

# Construct the data frame
col_names = ["name", "avg_family_size", "state", "cd"]
cd = pd.DataFrame(columns=col_names, data=r.json()[1:])

# We can check the values (by printing the head) 
# Of the avg_family_size column of the cd data frame.
# Print the head of the "avg_family_size" column
print(cd["avg_family_size"].head())

# Based on the values you saw in the avg_family_size column, we will set it to float data type.
# To Set the data type we will use the astype funciton and print
cd["avg_family_size"] = cd["avg_family_size"].astype(float)
print(cd)
