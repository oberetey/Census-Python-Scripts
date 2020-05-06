import requests
import pandas as pd
import seaborn as sns 


# This is the structure of the  intal point of access for the census database api
# Here you will need to create an appropriate string values to retrieve data for:
# year (2010) from dataset (Summary File 1 of the Decennial Census), base_url
# (for this prticular case of API usage in the case of US censu their is strict from to Build base URL)
HOST = "https://api.census.gov/data"
year = "2010"
dataset = "dec/sf1"
base_url = "/".join([HOST, year, dataset])

# now let's Specify variables and execute API request

# Here we are retrieveing data about a specfic type of residential dwelling for a specfic population type
# The dwelling is group qaurter,  which includes college dorms, correctional facilities, nursing homes, military bases, etc
# The population is incarated males under 18
# The variable code are similar but just a little off, in the second digit.
get_vars = ["NAME", "PCT021005", "PCT021015"]

# We define the predicates paramater and pass it to our get value
predicates["get"] = ",".join(get_vars)
r = requests.get(base_url, params=predicates)

# We provide the col_names with the header we want to improve readablitly for other who acces this data
col_names = ["name", "in_adult", "in_juvenile", "state"]

# Then we construct data frame and pass it to the variable states
states = pd.DataFrame(columns=col_names, data=r.json()[1:])

# Here we use astype to convert the columns in_adult and in_juvenile to integer
states[["in_adult", "in_juvenile"]] = states[["in_adult", "in_juvenile"]].astype(int)

# In order to calculate percentage of incarcerated male minors in adult facilities, we perform some varaible math.
states["pct_in_adult"] = 100 * states["in_adult"] / (states["in_adult"] + states["in_juvenile"])

# Here we set the sorting of the values,which will in turn reshape our graphic output
# This is done by sorting states by seeting:
# seeting (by) to pct_in_adult
# Setting (ascending) to false  giveing it descending order
# Setting inplace = True
states.sort_values(by = "pct_in_adult", ascending = False, inplace = True)

# Lastly we set, the x, y, and data values for the stripplot
sns.stripplot(x = "pct_in_adult", y = "name", data = states)
plt.show()
