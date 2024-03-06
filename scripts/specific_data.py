#!/usr/bin/env python3

import sys
import json, os, argparse
from pathlib import Path


parser = argparse.ArgumentParser(
    description='Selects specific data about elements and outputs it.',
    epilog=f"""Examples:
    Output files are written to the directory above {sys.argv[0]}.

    Properties written to a json file:
       $ {sys.argv[0]} --properties=name,atomic_mass --output name_mass.json

    Properties written to a csv file:
       $ {sys.argv[0]} --properties name,atomic_mass --output name_mass.csv

    Properties into files SpecificData.json and SpecificData.csv:
       $ {sys.argv[0]} --properties=name,atomic_mass

    Select properties interactively:
       $ {sys.argv[0]} --interactive""",
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
parser.add_argument('--properties', metavar='PROPERTY_NAMES', nargs=1,
                    help='properties to select as comma separated list')

parser.add_argument('--interactive', action="store_true",
                    help='whether to interactively select data')

parser.add_argument('--output', metavar='FILENAME', type=str, nargs=1,
                    help='where to output the data')

args = parser.parse_args()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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

full_path = os.getcwd().split('\\')
full_path.pop()

clear()
with open(os.path.join(Path(__file__).parents[1], 'PeriodicTableJSON.json'), encoding="utf8") as f:
    elements = json.load(f)['elements']

data_needed = {}
first_element = elements[0]

keys = first_element.keys()
if args.properties:
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

if args.interactive:
    for key in keys:
        while True:
            print(f'{c.BOLD + c.GREEN}{len(data_needed.keys())} Option(s) Selected: {c.END}{c.UNDERLINE}{list(data_needed.keys())}')
            print(f'{c.END}Do you need {c.BOLD + c.CYAN}{key}? {c.END}')
            needed = input(f'({c.GREEN}y/{c.RED}n{c.END}) [{c.PURPLE}default: {c.GREEN}y{c.END}]: ')
            if needed == 'y':
                data_needed[key] = True
            elif needed == 'n':
                break
            else:
                print('Invalid input')
                continue
            break
        clear()


if len(data_needed.keys()) == 0:
    print(c.RED + 'No properties selected.' + c.END)
    exit()

def writeCSV():
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
def writeJSON():
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

output = 'SpecificData'
printz = ''
if args.output:
    if ('json' in args.output[0].lower()) or ('csv' in args.output[0].lower()):
        output = args.output[0].replace('.json', '').replace('.csv', '')

    if 'json' in args.output[0].lower():
        writeJSON()
        exit()
    if 'csv' in args.output[0].lower():
        writeCSV()
        exit()
else:
    writeJSON()
    writeCSV()