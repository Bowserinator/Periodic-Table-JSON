A Python library of periodic data. The non-list 


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
    
