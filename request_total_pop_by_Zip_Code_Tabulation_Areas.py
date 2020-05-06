# In the marketing field, it is very common to want to know ZIP Code demographics. 
# ZIP Code Tabulation Areas ("ZCTAs") are Census-defined equivalents to
# ZIP Codes that are built out of Census blocks. 
# In this exercise you will request total population for all ZCTAs in the state of Alabama.

# In pandas, an index can be used to retrieve particular rows. 
# The GEOIDs are suitable row identifiers. 
# In this exercise you will set a multilevel index based on the state and ZCTA of each row.

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
# "P001001" (total population)
# Specify Census variables and other predicates
# predicates here is the output the APi with provide,
# "get" strucues the requests.
# "for" specficy the geographic level

# Build dictionary of predicates and execute the request
predicates = {}
predicates["get"] = ",".join(["NAME",  "P001001"])

# Set the "for" key in the predicates dict to return all ZCTAs; 
# Spell out the geography in full as "zip code tabulation area (or part) followed by (:*)""
predicates["for"] = "zip code tabulation area (or part):*"

# Set the "in" key in the predicates dict to only return ZCTAs in the state of Alabama; 
# You will have to look up the FIPS code for Alabama in one of the online sources
predicates["in"] = "state:01"
r = requests.get(base_url, params=predicates)

# Construct the data frame
col_names = ["name", "total_pop", "state", "zcta"]
zctas = pd.DataFrame(columns=col_names, data=r.json()[1:])
zctas["total_pop"] = zctas["total_pop"].astype(int)

# Set the data frame index to be the concatenation of the state and zcta columns. 
# Use inplace = True to not create a new data frame.
# this will set multilevel index from GEOIDs and print the head
zctas.set_index(['state', 'zcta'], inplace = True)
print(zctas.head())
