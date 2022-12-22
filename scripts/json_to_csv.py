#!/usr/bin/env python3
"""
Convert the JSON data to CSV
"""

import json
import pandas

PERIODIC_TABLE_CSV = "../PeriodicTableCSV.csv"

# Validate and load data
from validate_json import PERIODIC_TABLE_JSON
with open(PERIODIC_TABLE_JSON) as jfile:
    jdata = json.load(jfile)["elements"]

# Normalize and save to CSV
# See: https://stackoverflow.com/a/58648286/2038713
df = pandas.json_normalize(jdata)
print(df)
df.to_csv(PERIODIC_TABLE_CSV, index=False)
print(f"CSV saved to {PERIODIC_TABLE_CSV}")
