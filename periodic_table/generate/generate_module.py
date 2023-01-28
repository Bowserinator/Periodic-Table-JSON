#!/usr/bin/env python3
import argparse
import collections
import json
import logging
import os
from typing import List

_logger = logging.getLogger(__name__)
_ALIASES = (
    #British spellings
    (13,('aluminium',)),
    (16,('sulphur',)),
)

_ELEMENT_START= """# generated from JSON file. Do not hand edit
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import Iterable, List, Optional


@dataclass_json
@dataclass
class Element:
    name: str
    atomic: int
    symbol: str"""

_ELEMENT_TAIL ="""    _altnames : List[str] = field(default_factory=list)

    def setnames(self,names:Iterable[str])->None: 
        self._altnames = [n.lower()  for n in names]
        
        
    def is_named(self,value)->bool:
        \"""Case-insensitive search of names\"""
        svalue = value.lower()
        return svalue == self.name.lower() or svalue in self._altnames
"""


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



class CodeBuilder:

    def __init__(self):
        src = os.path.join(os.path.dirname(__file__),'..','..','PeriodicTableJSON.json')
        self.jsource = os.path.abspath(src)
        if not os.path.isfile(self.jsource):
            raise ValueError(f"{self.jsource} not found")

    def __enter__(self):
        script = os.path.join(os.path.dirname(__file__),'..','src','periodic_table','table.py')
        self.code = open(script,'w')
        print(_ELEMENT_START, file=self.code)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.code.close()
        pass


    def generate(self):
        self._read_json()
        self._build_element()
        self._build_table()

    def _read_json(self):
        attrs = collections.defaultdict(int)
        with open (self.jsource) as f:
            data = json.load(f)
        self.raw_data = data['elements']
        for e in self.raw_data:
            for d in e.keys():
                attrs[d] += 1
        expected = list(attrs.values())[0]
        bad = False
        for a, num in attrs.items():
            if num != expected:
                print(f"{a} has {num} implementors, not {expected}")
                bad = True
        if bad:
            raise ValueError("length mismatch")
        return attrs

    def _cleanup(self,identifier):
        """Cleanup JSON value into valid Python identifier"""
        return identifier.replace('-','_')

    def _build_element(self):
        _SUPPORTED = (str,float,int)
        #start with these
        self.field_order : List[str] = ['name','number','symbol']
        example = self.raw_data[0]
        for  attr in self.field_order:
            if attr not in example:
                raise ValueError(f'{attr} missing')
        adding = []
        for k,v in example.items():
            _logger.debug(f"{k} {type(v)}")
            if k in self.field_order:
                continue
            if type(v) not in _SUPPORTED:
                _logger.info(f"Skipping {k} {type(v)}")
                continue
            adding.append(k)
        adding = sorted(adding)
        self.field_order.extend(adding)
        _logger.debug(self.field_order)
        for field in adding:
            v = example[field]
            tsting = type(v).__name__
            print(f'    {self._cleanup(field)} : Optional[{tsting}]',file=self.code)
        print(_ELEMENT_TAIL,file=self.code)

    def _build_table(self):
        print(_PERIODIC_START, file=self.code)
        for e in self.raw_data:
            print(12*' ' +'Element(',end='',file=self.code)
            values = []
            for fld in self.field_order:
                value = e[fld]
                if isinstance(value,str):
                    values.append(f'"""{value}"""')
                else:
                    values.append(str(value))
            print(f"{','.join(values)}),",file=self.code)
        print(8*' ' +')',file=self.code)
        for atomic, names in _ALIASES:
            namestrs = [f"'{n}'" for n in names]
            setter = f"        self.search_number({atomic}).setnames([{','.join(namestrs)}])"
            print(setter, file=self.code)


        print(_PERIODIC_TAIL,file=self.code)




def main():
    logging.basicConfig()
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-l', '--loglevel', default='WARN', help="Python logging level")

    args = parser.parse_args()
    _logger.setLevel(getattr(logging,args.loglevel))
    with CodeBuilder() as builder:
        builder.generate()


if __name__ == "__main__":
    main()
