#
# Template for PeriodicTable class
#
_PERIODIC_START = """

class PeriodicTable:

    def __init__(self):
        self.elements =  ("""

_PERIODIC_TAIL = """    def search_name(self,name:str)-> Optional[Element]:
        \"""Case-insensitive British / American search for element name\"""
        for e in self.elements:
            if e.is_named(name):
                return e
        return None

    def search_symbol(self,symbol:str)-> Optional[Element]:
        \"""Case-insensitive search for element symbol\"""
        lsymbol = symbol.lower()
        for e in self.elements:
            if lsymbol == e.symbol.lower():
                return e
        return None

    def search_number(self,number:int)-> Optional[Element]:
        \"""Search by atomic number\"""
        for e in self.elements:
            if e.atomic == number:
                return e
        return None
"""
