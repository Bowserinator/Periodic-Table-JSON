from generate.updated_definition import PeriodicTable

pt = PeriodicTable()
for e in pt.elements:
    print(f"{e.name} {e.atomic}")
s = pt.search_number(16)
print(s)
