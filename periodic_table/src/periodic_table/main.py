#!/usr/bin/env python3
import argparse
import dataclasses
import logging
from pprint import pprint

from periodic_table import PeriodicTable


def main():
    logging.basicConfig()
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()

    group.add_argument('--name',help="search by element name")
    group.add_argument('--number',type=int, help="search by atomic number")
    group.add_argument('--symbol', help="search by symbol")

    args = parser.parse_args()
    pt = PeriodicTable()
    e = None
    if args.name:
        e = pt.search_name(args.name)
    if args.number:
        e = pt.search_number(args.number)
    if args.symbol:
        e = pt.search_symbol(args.number)
    if e:
        pprint(dataclasses.asdict(e))



if __name__ == "__main__":
    main()

