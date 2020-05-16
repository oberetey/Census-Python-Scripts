# The Affordable Care Act went into effect in 2014. 
# One of its goals was to increase health insurance coverage among healthy young adults. 
# Has health insurance coverage among 19-25 year olds changed with the
# passage of the Affordable Care Act? 
# Let's calculate the percentage point change in coverage by state. 
# Then plot the change against the initial percent covered rate.

# ACS Table B27022 - "Health Insurance Coverage Status By Sex By
# Enrollment Status For Young Adults Aged 19 To 25" has been loaded. 
# Columns names (printed to the console) indicate breakdowns
# by sex (m/f), school enrollment (school/noschool) and insurance (insured/uninsured).

import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# This is the structure of the  intal point of access for the census database api
# Here you will need to create an appropriate string values to retrieve data for:
# year (2010) from dataset (Summary File 1 of the Decennial Census), base_url
# (for this prticular case of API usage in the case of US censu their is strict from to Build base URL)
HOST = "https://api.census.gov/data"
year = "2014"
dataset = "acs/acs1"
base_url = "/".join([HOST, year, dataset])

# now let's Specify variables and execute API request

# Here we are retrieveing data about a specfic type of residential dwelling for a specfic population type
# The dwelling is group qaurter,  which includes college dorms, correctional facilities, nursing homes, military bases, etc
# The population is incarated males under 18
# The variable code are similar but just a little off, in the second digit.
get_vars = ["B27022_" + str(i + 1).zfill(3) + "E" for i in range(15)]
get_vars = ["NAME"] + get_vars


predicates = {}
# We define the predicates paramater and pass it to our get value
predicates["get"] = ",".join(get_vars)
predicates["for"] = "state:*"
r = requests.get(base_url, params=predicates)

col_names = ["state", "total", "m", "m_school", "m_school_insured",
             "m_school_uninsured", "m_noschool", "m_noschool_insured",
             "m_noschool_uninsured", "f", "f_school", "f_school_insured",
             "f_school_uninsured", "f_noschool", "f_noschool_insured",
             "f_noschool_uninsured", "country"]

pre_states = pd.DataFrame(columns = col_names, data=r.json()[0:])

states = pre_states.iloc[1:].copy()
print(states)

states[["total"]] = states[["total"]].astype(int)
states[["m_school_insured"]] = states[["m_school_insured"]].astype(int)
states[["m_noschool_insured"]] = states[["m_noschool_insured"]].astype(int)
states[["f_school_insured"]] = states[["f_school_insured"]].astype(int)
states[["f_noschool_insured"]] = states[["f_noschool_insured"]] .astype(int)

# first we Calculate percent insured
states["insured_total"] = states["m_school_insured"] + states["m_noschool_insured"] + states["f_school_insured"] + states["f_noschool_insured"]
# next  we Calculate the percentage insured as 100 times the insured_total, divided by the total population

states["pct_insured"] = 100 * (states["insured_total"]/states["total"])
print(states)


