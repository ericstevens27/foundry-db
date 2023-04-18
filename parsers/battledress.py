from parsers import armor


def parse(line):
    tokens = armor.parse(line)
    tokens = tokens[:-3] + [' '.join(tokens[-3:])]
    return tokens


def columns():
    return [
        'Armour Type',
        'Protection',
        'Secondary',
        'Secondary Type',
        'TL',
        'Rad',
        'STR',
        'DEX',
        'Slots',
        'Kg',
        'Cost',
        'Required Skill'
    ]
