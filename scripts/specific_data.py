import json, os

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

path = str('\\'.join(full_path)) + '\\PeriodicTableJSON.json'

with open(path, encoding="utf8") as f:
    elements = json.load(f)['elements']

data_needed = {}
first_element = elements[0]

keys = first_element.keys()

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


with open(r'../SpecificJSON.json', 'w') as f:
    elem_to_write = []

    for element in elements:
        e = {}
        for key in data_needed:
            if data_needed[key]:
                e[key] = element[key]
        elem_to_write.append(e)

    f.write(json.dumps(elem_to_write, indent=4))
    f.write('\n')