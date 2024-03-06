#!/usr/bin/env python3

import sys
import json, os, argparse
from pathlib import Path


class c:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def create_commandeline_parser(default_file):
    parser = argparse.ArgumentParser(
        description='Selects specific data about elements and outputs it.',
        epilog=f"""Examples:
        NOTE: output files are written to the directory above {sys.argv[0]}.

        Properties written to a json file:
           $ {sys.argv[0]} --properties=name,atomic_mass --output name_mass.json

        Properties written to a csv file:
           $ {sys.argv[0]} --properties name,atomic_mass --output name_mass.csv

        Properties written into both files {default_file}.json and {default_file}.csv:
           $ {sys.argv[0]} --properties=name,atomic_mass

        Union of properties written into both files {default_file}.json and {default_file}.csv:
           $ {sys.argv[0]} --properties=name,atomic_mass --interactive

        Select properties interactively and write to files {default_file}.json and {default_file}.csv:
           $ {sys.argv[0]} --interactive
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('--properties', metavar='P1,...', nargs=1,
                        help='comma separated list of properties')

    parser.add_argument('--interactive', action="store_true",
                        help='whether to interactively select data')

    parser.add_argument('--output', metavar='FILENAME', nargs='?', const=default_file, default='',
                        help=f'where to output the data (default: {default_file}.{{json,csv}})')
    return parser


def read_periodic_table():
    with open(os.path.join(Path(__file__).parents[1], 'PeriodicTableJSON.json'), encoding="utf8") as f:
        elements = json.load(f)['elements']
    return elements


def parse_properties(data_needed, args, keys):
    properties = args.properties[0]
    props = []
    z = ""
    for x in properties:
        if x == ',':
            props.append(z)
            z = ""
        else:
            z += x
    if z != "":
        props.append(z)

    for prop in props:
        if prop not in keys:
            print(c.RED + 'Property ' + prop + ' not found.' + c.END)
            props.remove(prop)
        else:
            data_needed[prop] = True
            print(c.GREEN + 'Property ' + prop + ' found.' + c.END)

    for p in props:
        data_needed[p] = True
    return data_needed


def parse_interactive(data_needed, keys):
    for key in keys:
        if key in data_needed:   # Already selected, move to next
            continue
        needed = ''
        while True:
            print(f'{c.BOLD + c.GREEN}{len(data_needed.keys())} Option(s) Selected '
                  f'{c.END}{c.UNDERLINE}{list(data_needed.keys())}')
            print(f'{c.END}Do you need {c.BOLD + c.CYAN}{key}? {c.END}')
            needed = input(f'({c.GREEN}y/{c.RED}n{c.END}/{c.BLUE}q(uit){c.END}) [{c.PURPLE}default: {c.GREEN}y{c.END}]: ')
            if needed == 'y':
                data_needed[key] = True
            elif needed == 'n':
                break
            elif needed == 'q':
                break
            else:
                print('Invalid input')
                continue
            break
        if needed == 'q':
            break
        clear()
    return data_needed


def save2file(args, elements, data_needed, default_file):
    if not args.output or args.output == default_file:   # Use default and write to both csv and json files.
        writeJSON(default_file, elements, data_needed)
        writeCSV(default_file, elements, data_needed)
    else:                                                # Write to provided file name.
        if ('json' in args.output.lower()) or ('csv' in args.output.lower()):
            output = args.output.replace('.json', '').replace('.csv', '')
        if 'json' in args.output.lower():
            writeJSON(output, elements, data_needed)
        if 'csv' in args.output.lower():
            writeCSV(output, elements, data_needed)


def writeCSV(output, elements, data_needed):
    with open(os.path.join(Path(__file__).parents[1], output + '.csv'), 'w', encoding="utf8") as f:
        elem_to_write = []
        elem_to_write.append(','.join(data_needed.keys()))
        for element in elements:
            e = ""
            for key in data_needed:
                if data_needed[key]:
                    e += str(element[key]) + ','
            if(e[-1] == ','):
                e = e[:-1]
            elem_to_write.append(e)

        f.write("\n".join(elem_to_write))
        f.write('\n')


def writeJSON(output, elements, data_needed):
    with open(os.path.join(Path(__file__).parents[1], output + '.json'), 'w') as f:
        elem_to_write = []

        for element in elements:
            e = {}
            for key in data_needed:
                if data_needed[key]:
                    e[key] = element[key]
            elem_to_write.append(e)

        f.write(json.dumps(elem_to_write, indent=4))
        f.write('\n')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    default_file = 'SpecificData'
    parser = create_commandeline_parser(default_file)

    args = parser.parse_args()
    elements = read_periodic_table()

    clear()

    keys = elements[0].keys()
    data_needed = {}
    if args.properties:
        data_needed = parse_properties(data_needed, args, keys)
    if args.interactive:
        data_needed = parse_interactive(data_needed, keys)

    if data_needed:
        save2file(args, elements, data_needed, default_file)
    else:
        print(c.RED + 'No properties selected.' + c.END)
