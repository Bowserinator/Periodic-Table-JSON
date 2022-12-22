#!/usr/bin/env python3
"""
Validate that the JSON data is correctly formatted according
to the template in the 'schemas' directory.
"""

import json
import jsonschema

PERIODIC_TABLE_JSON = "../PeriodicTableJSON.json"
PERIODIC_TABLE_SCHEMA = "../schemas/periodicTableJSON.schema"

print(f"Validating {PERIODIC_TABLE_JSON} against {PERIODIC_TABLE_SCHEMA}")
with open(PERIODIC_TABLE_JSON) as jfile, open(PERIODIC_TABLE_SCHEMA) as sfile:
    data = json.load(jfile)
    schema = json.load(sfile)
# Raises an exception in case of failure
jsonschema.validate(instance=data,schema=schema)

print("Validation passed")
