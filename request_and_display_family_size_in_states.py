#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# accesing the and requesting from the api





# In this exercise, you will construct an API request to retrieve:
# the average family size, and median age for all states in the United States. 
# The data will come from Summary File 1 of the 2010 Decennial Census.

# to begin you will need to import requests
import requests

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
predicates["for"] = "state:*"

# Output r.text using the print function
# this is done by passing requests.get method:
# base_url, and  the params specficed to for the predicates value to
# lastly Execute the request, examine text of response object
r = requests.get(base_url, params=predicates)
print(r.text)


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# transforming the api response





# In this exercise you will load data from an API response object into a pandas data frame. 
# You will assign user-friendly column names and convert the values from strings to appropriate data types.

# After creating the data frame, run the sample code to create a scatterplot to visualize:
# the relationship between average family size and median age in the United States.

import requests
import pandas as pd

# A response object r is loaded.

# Import seaborn
import seaborn as sns
sns.set()

# Here we construct a dataframe that will used in a scatterplot.
# At this stage we are conducting tranfromation of the data pull and held by the varible r.
# To ideantify the columns in this dataframe we contruct column names:
# name, median_age, avg_family_size, and state

# Construct the DataFrame
col_names = ["name", "median_age", "avg_family_size", "state"]

# DataFrame variable will be states,
# Use the data frame constructor to create the data frame states, 
# passing the col_names variable to the columns parameter
#The data parameter should be set to r.json(), but use slicing to skip the first item, which contains the old column names
states = pd.DataFrame(columns = col_names, data = r.json()[1:])

# now that the dataframe is stored in the states, 
# we can use the astype method on each column to assign the correct data type.
# Convert each column with numeric data to a float type, with .astype(float) 
states["median_age"] = states["median_age"].astype(float)
states["avg_family_size"] = states["avg_family_size"].astype(float)

# Scatterplot with regression line
sns.lmplot(x = "avg_family_size", y = "median_age", data = states)
plt.show()
