# California's major cities have been in the news for skyrocketing housing prices. 
# How has the median home value changed over the last several years? 

import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# In this exercise you will use a loop to request variable B25077_001E from seven ACS years and plot the value over time.

# The predicates dictionary has been created, and is printed to the console. 
# Notice that state:06 sets the GEOID for California. 

# This is the structure of the  intal point of access for the census database api
# Here you will need to create an appropriate string values to retrieve data for:
# Year (2010) from dataset (Summary File 1 of the Decennial Census), base_url
# (for this prticular case of API usage in the case of US censu their is strict from to Build base URL)
HOST = "https://api.census.gov/data"
# Notice here the dataset is the American Community Survey.
# Depending on the dataset this value could be different.
# You will get an error messges if you reference the wrong dataset
dataset = "acs/acs1"

# Construct get_vars, which is the list of Census variables to request, 
# if you were usign the dec/sf1 dataset you could go with the following variable names: 
# "NAME"(well be fit the geogrpahicy level in predicates), 
# "P013001" (median age),
# "P037001" (average family size)
# here we dont need these so ignore the above in this case. 
# Specify Census variables and other predicates
# Predicates here is the output the APi with provide,
# "get" strucues the requests.
# "for" specficy the geographic level
get_vars = ["NAME", "B25077_001E"]
predicates = {}
predicates["get"] = ",".join(get_vars)
predicates["for"] = "state:06"

# HOST and dataset have been defined, and dfs is an empty list that has been initialized as a 
# collector for the requested data frames.
col_names = ["name", "median_home_value", "state"]
#here we initalize the empty collector
dfs = []
# Loop over years 2011 to 2017
# this can be done by constructing a range object with integers from 2011 to 2017
# The range object will start at the year desired, and end one year above the end year desired
# As such range(2011, 2017)
for year in range(2011, 2018):
    base_url = "/".join([HOST, str(year), dataset])
    r = requests.get(base_url, params=predicates)
    df = pd.DataFrame(columns=col_names, data=r.json()[1:])    
    # To add  acolumn to df to hold year value, pass the variable year to a new column for year, 
    # done as such df['year']
    
    df['year'] = year
    # to append df to collector dfs, just apply the function append, and pass the df variable
    dfs.append(df)

# Concatenate all data frames, fix column type
states = pd.concat(dfs)
# Set the median_home_value column data type to int by using the .astype fucntion and pass it the int data type.
states["median_home_value"] = states["median_home_value"].astype(int)

# Create a lineplot of home values. Set the first parameter (x) to "year", set second parameter (y) to "median_home_value", (data) is of the df states
sns.lineplot(x = "year", y = "median_home_value", data = states)
plt.show()
