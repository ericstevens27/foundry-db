import json

def extractIcon(l:str)->dict:
    # -a----        2023-04-16   5:40 PM           1763 gauss-pistol.svg
    lineOut = {}
    indexLastSpace = l.strip().rindex(' ')
    imgName = l[indexLastSpace:].strip()
    lineOut['img'] = imgName
    rawName = imgName[:-4]
    nameElements = []
    if rawName.find('-') != -1:
        nameElements = rawName.split('-')
    else:
        if rawName.find('_') != -1:
            nameElements = rawName.split('_')
        else:
            nameElements.append(rawName)
    lineOut['tags'] = nameElements
    return lineOut

def main ():
    iconFileName = 'icons.txt'
    iconOutput = {"icons": []}
    iconOutputfile = 'icon.json'
    with open(iconFileName, "r", encoding="utf-16") as iconFD:
        for line in iconFD:
            if line == '\n':
                continue
            else:
                iconOutput['icons'].append(extractIcon(line))
    iconOutputFD = open(iconOutputfile, 'w')
    json.dump(iconOutput, iconOutputFD, ensure_ascii=True, indent=4)
    return True

if __name__ == "__main__":
    main()
