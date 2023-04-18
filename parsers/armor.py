import re


def parse_secondary(text):
    text = text.strip()
    if 'PSI' in text:
        tokens = [text.replace(' PSI', ''), 'PSI']
    else:
        tokens = text.split(' vs. ')
    tokens[0] = tokens[0].replace('+','')
    tokens = list(s.strip() for s in tokens)
    return tokens[0], tokens[1]


def parse(line):
    plus_split = line.split('+', 1)
    name = plus_split[0]
    specs = plus_split[1]
    secondary_protection = ''
    secondary_protection_type = ''
    if '(' in specs:
        secondary = re.search(r'\((.*)\)', specs)
        secondary = secondary.group(1)
        specs = specs.replace(f'({secondary}) ', '')
        secondary_protection, secondary_protection_type = parse_secondary(secondary)
    tokens = specs.split(' ')
    tokens = tokens[:1] + [secondary_protection, secondary_protection_type] + tokens[1:]
    return [name.strip()] + tokens


def columns():
    return [
        'Armour Type',
        'Protection',
        'Secondary',
        'Secondary Type',
        'TL',
        'Rad',
        'Kg',
        'Cost',
        'Required Skill'
    ]