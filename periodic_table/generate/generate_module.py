#!/usr/bin/env python3
import argparse
import collections
import datetime
import json
import logging
import os
from typing import List

from element_template import _ELEMENT_START, _ELEMENT_TAIL
from table_template import _PERIODIC_START, _PERIODIC_TAIL
from readme_template import _README

_logger = logging.getLogger(__name__)
_ALIASES = (
    # British spellings
    (13, ('aluminium',)),
    (16, ('sulphur',)),
)

JSON_SOURCE = 'PeriodicTableJSON.json'


class CodeBuilder:

    def __init__(self):
        self.our_directory = os.path.dirname(__file__)
        src = os.path.join(self.our_directory, '..', '..', JSON_SOURCE)
        self.jsource = os.path.abspath(src)
        if not os.path.isfile(self.jsource):
            raise ValueError(f"{self.jsource} not found")
        self.skipped : List[str] = []

    def __enter__(self):
        script = os.path.join(os.path.dirname(__file__), '..', 'src', 'periodic_table', 'table.py')
        self.code = open(script, 'w')
        self.datestamp = datetime.datetime.now().strftime('%Y %b %d')
        print(f'# generated from {JSON_SOURCE} {self.datestamp}. Do not hand edit',file=self.code)
        print(_ELEMENT_START, file=self.code)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.code.close()
        pass


    def generate(self):
        self._read_json()
        self._build_element()
        self._build_table()
        self._generate_readme()

    def _read_json(self):
        attrs = collections.defaultdict(int)
        with open(self.jsource) as f:
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

    def _cleanup(self, identifier):
        """Cleanup JSON value into valid Python identifier"""
        return identifier.replace('-', '_')

    def _build_element(self):
        _SUPPORTED = (str, float, int)
        # start with these
        self.field_order: List[str] = ['name', 'number', 'symbol']
        example = self.raw_data[0]
        for attr in self.field_order:
            if attr not in example:
                raise ValueError(f'{attr} missing')
        adding = []
        for k, v in example.items():
            _logger.debug(f"{k} {type(v)}")
            if k in self.field_order:
                continue
            if type(v) not in _SUPPORTED:
                _logger.info(f"Skipping {k} {type(v)}")
                self.skipped.append(k)
                continue
            adding.append(k)
        adding = sorted(adding)
        self.field_order.extend(adding)
        _logger.debug(self.field_order)
        for field in adding:
            v = example[field]
            tsting = type(v).__name__
            print(f'    {self._cleanup(field)} : Optional[{tsting}]', file=self.code)
        print(_ELEMENT_TAIL, file=self.code)

    def _build_table(self):
        print(_PERIODIC_START, file=self.code)
        for e in self.raw_data:
            print(12 * ' ' + 'Element(', end='', file=self.code)
            values = []
            for fld in self.field_order:
                value = e[fld]
                if isinstance(value, str):
                    values.append(f'"""{value}"""')
                else:
                    values.append(str(value))
            print(f"{','.join(values)}),", file=self.code)
        print(8 * ' ' + ')', file=self.code)
        for atomic, names in _ALIASES:
            namestrs = [f"'{n}'" for n in names]
            setter = f"        self.search_number({atomic}).setnames([{','.join(namestrs)}])"
            print(setter, file=self.code)

        print(_PERIODIC_TAIL, file=self.code)

    def _generate_readme(self):
        missing = ', '.join([f'*{m}*' for m in self.skipped])
        with open(os.path.join(self.our_directory,'..','README.md'),'w') as f:
            print(_README.format(datestamp=self.datestamp,missing=missing),file=f)




def main():
    logging.basicConfig()
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-l', '--loglevel', default='WARN', help="Python logging level")

    args = parser.parse_args()
    _logger.setLevel(getattr(logging, args.loglevel))
    with CodeBuilder() as builder:
        builder.generate()


if __name__ == "__main__":
    main()
