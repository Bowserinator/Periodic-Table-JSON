#
# template for Element dataclass
#
_ELEMENT_START= """import io
from dataclasses import dataclass, field,fields
from dataclasses_json import dataclass_json
from typing import Iterable, List, Optional


@dataclass_json
@dataclass
class Element:
    name: str
    atomic: int
    symbol: str"""

_ELEMENT_TAIL ="""    _altnames : List[str] = field(default_factory=list)

    def __str__(self):
        buffer = io.StringIO()
        print(f'Element {self.name}',file=buffer)
        names = [f.name for f in fields(self) if not f.name.startswith('_') and f.name != 'name']
        nlen = max([len(n) for n in names])
        for name in names:
            print(f'    {name:{nlen}} = {getattr(self,name)}',file=buffer)
        return buffer.getvalue()

    def setnames(self,names:Iterable[str])->None: 
        self._altnames = [n.lower()  for n in names]
        
        
    def is_named(self,value)->bool:
        \"""Case-insensitive search of names\"""
        svalue = value.lower()
        return svalue == self.name.lower() or svalue in self._altnames
"""
