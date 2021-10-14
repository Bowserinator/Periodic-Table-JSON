#!/usr/bin/env python3
"""
Convert the JSON data to CSV
"""

import json
import pandas

PERIODIC_TABLE_CSV = "PeriodicTableCSV.csv"

# Validate and load data
from validate_json import PERIODIC_TABLE_JSON
with open(PERIODIC_TABLE_JSON) as jfile:
    jdata = json.load(jfile)["elements"]

# Normalize and save to CSV
# See also: https://stackoverflow.com/questions/1871524/how-can-i-convert-json-to-csv
df = pandas.json_normalize(jdata)
print(df)
df.to_csv(PERIODIC_TABLE_CSV)
print(f"CSV saved to {PERIODIC_TABLE_CSV}")
