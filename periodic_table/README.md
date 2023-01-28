A Python library of periodic data statically generated from **PeriodicTableJSON.json**  (https://github.com/NMRbox/Periodic-Table-JSON) on 2023 Jan 28.

An *Element* dataclass and *PeriodicTable* container class is generated from the JSON data.

Currently only the single valued str, float, and int are supported. The JSON fields *shells*, *ionization_energies*, *image* are omitted. 


# Installation 
  pip install periodic_table

# Usage

    from periodic_table import PeriodicTable
    pt = PeriodicTable()
    h = pt.search_name('hydrogen')
    s = pt.search_number(16)
    fe = pt.search_symbol('Fe')
    for element in pt.elements:
        print(element)

# Discussion
### Unnecessary
This module is not necessary to use PeriodicTableJSON.json in Python. 

     with open('PeriodicTableJSON.json') as f:
            data = json.load(f)
    elements = data['elements']

will bring all data into Pyton as nested data structure.

### Convenient
The module was implemented for the convenience of named class fields. A static definition allows type
checking and code completion when working in Python integrated development environments (IDE).

### Additional feature
The *PeriodicTable.search_name* features supports the British spellings *aluminium* and *sulphur*.

