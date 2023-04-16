import csv
import json
from pathlib import Path
import secrets

# import random
# import string   

# def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
#         return ''.join(random.choice(chars) for _ in range(size))   

def setDbRecord(type:str)->dict:
    record = {
        "name": "",
        "type": "",
        "img": "",
        "system": {
            "name": "",
            "techLevel": 0,
            "description": "",
            "shortdescr": "",
            "quantity": 0,
            "weight": 0,
            "price": 0,
            "traits": [],
            "consumables": [],
            "skillModifier": 0,
            "skill": "",
            "associatedSkillName": "",
            "equipped": "",
            "docReference": "",
            "pdfReference": {
                "type": "",
                "href": "",
                "label": ""
            },
        },
        "effects": [],
        "flags": {
            "twodsix": {
                "newItem": True
            },
            "core": {
                "sourceId": "Item.viNh0N8Fw28bpV2e"
            }
        },
        "_stats": {
            "systemId": "twodsix",
            "systemVersion": "2.27.3",
            "coreVersion": "10.291",
            "createdTime": 1681493070337,
            "modifiedTime": 1681493265527,
            "lastModifiedBy": "OK9YthkIIxCpCkT0"
        },
        "folder": None,
        "sort": 0,
        "ownership": {
            "default": 0,
            "OK9YthkIIxCpCkT0": 3
        },
        "_id": ""
    }
    if type == "armor":
        record['type'] = 'armor'
        record['system']['armor'] = 0
        record['system']['secondaryArmor'] = {
            'value': 0,
            'protectionTypes': []
        }
        record['system']['radiationProtection'] = {
            'value': 0
        }
    if type == "weapon":
        record['type'] = 'weapons'
        record['system']['target'] = {
            "value": None,
            "width": None,
            "units": "m",
            "type": "none"
        }
        record['system']['range'] = "0"
        record['system']['damage'] = "0"
        record['system']['damageBonus'] = 0
        record['system']['magazineSize'] = 0
        record['system']['ammo'] = "0"
        record['system']['lawLevel'] = 0
        record['system']['magazineCost'] = 0
        record['system']['rangeBand'] = ""
        record['system']['weaponType'] = ""
        record['system']['damageType'] = ""
        record['system']['rateOfFire'] = "1"
        record['system']['recoil'] = False
        record['system']['armorPiercing'] = 0
        record['system']['handlingModifiers'] = ""
    return record

def makeFolder(folderName:str)->dict:
    folder = {
        "name": "#[CF_tempEntity]",
        "type": "equipment",
        "flags": {
            "cf": {
                "id": "",
                "name": "",
                "color": "#000000",
                "fontColor": "#FFFFFF",
                "icon": "",
                "sorting": "a",
                "contents": [
                ],
                "children": []
            },
            "twodsix": {
                "newItem": True
            }
        },
        "img": "icons/svg/item-bag.svg",
        "system": {
            "name": "",
            "techLevel": 0,
            "description": "",
            "shortdescr": "",
            "quantity": 1,
            "weight": 0,
            "price": "",
            "traits": [],
            "consumables": [],
            "skillModifier": 0,
            "skill": "",
            "associatedSkillName": "",
            "equipped": "backpack",
            "docReference": "",
            "pdfReference": {
                "type": "",
                "href": "",
                "label": ""
            },
            "type": "equipment",
            "useConsumableForAttack": ""
        },
        "effects": [],
        "folder": None,
        "sort": 0,
        "ownership": {
            "default": 0,
            "ciibqOqESKGj7NAB": 3
        },
        "_stats": {
            "systemId": "twodsix",
            "systemVersion": "2.27.3",
            "coreVersion": "10.291",
            "createdTime": 1681607177109,
            "modifiedTime": 1681607186985,
            "lastModifiedBy": "ciibqOqESKGj7NAB"
        },
        "_id": ""
    }
    folder['flags']['cf']['name'] = folderName
    folder['flags']['cf']['id'] = secrets.token_hex(8)
    folder['_id'] = secrets.token_hex(8)
    return folder

def makeOutputRecord(csvData:dict, type:str, folders:dict)->dict:
    imgRoot = 'systems/twodsix/assets/icons/'
    # set base field values
    outputRecord = setDbRecord(type)
    outputRecord["_id"] = secrets.token_hex(8)
    
    # first check for a folder
    # folder dict struct is type array containing name pointing to folder record

    # folders are disabled

    # if csvData['folder'] != 'none':
    #     # we want to put this record into a folder
    #     # does the folder already exist?
    #     if csvData['folder'] in folders[type]:
    #         # pull the record so we can add this id to the contents
    #         folders[type][csvData['folder']]['flags']['cf']['contents'].append(outputRecord['_id'])
    #     else:
    #         # new record - make the folder
    #         recordFolder = makeFolder(csvData['folder'])
    #         recordFolder['flags']['cf']['contents'].append(outputRecord['_id'])
    #         # push update back into folders
    #         folders[type][csvData['folder']] = recordFolder

    outputRecord['img'] = imgRoot+csvData['image']
    outputRecord['system']['folder'] = None
    if int(csvData['techlevel']) < 10:
        suffixTL = " (TL  "+csvData['techlevel']+")"
    else:
        suffixTL = " (TL "+csvData['techlevel']+")"
    outputRecord['name'] = csvData['name']+" (TL "+csvData['techlevel']+")"
    outputRecord['system']['name'] = csvData['name']
    if csvData['shortdescription']:
        outputRecord['system']['shortdescr'] = csvData['shortdescription']
    if csvData['description']:
        outputRecord['system']['description'] = csvData['description']
    outputRecord['system']['skill'] = csvData['skill']
    outputRecord['system']['techLevel'] = int(csvData['techlevel'])
    outputRecord['system']['quantity'] = int(csvData['quantity'])
    outputRecord['system']['weight'] = int(csvData['weight'])
    outputRecord['system']['price'] = int(csvData['price'])

    if type == 'armor':
        # insert custom bits for this type
        outputRecord['system']['armor'] = int(csvData['armor'])
        if csvData['secondaryarmor'] != '':
            outputRecord['system']['secondaryArmor']['value'] = int(csvData['secondaryarmor'])
            for t in csvData['secondarytypes'].split(":"):
                outputRecord['system']['secondaryArmor']['protectionTypes'].append(t)
        if csvData['radiation'] != '':
            outputRecord['system']['radiationProtection']['value'] = int(csvData['radiation'])
    else:
        if type == 'weapon':
            # insert custom bits for this type
            outputRecord['system']['range'] = csvData['range']
            outputRecord['system']['damage'] = csvData['damage']
            outputRecord['system']['damageBonus'] = int(csvData['damagebonus'])
            outputRecord['system']['magazineSize'] = int(csvData['magsize'])
            outputRecord['system']['ammo'] = csvData['ammo']
            outputRecord['system']['lawLevel'] = int(csvData['lawlevel'])
            outputRecord['system']['magazineCost'] = int(csvData['magcost'])
            outputRecord['system']['rangeBand'] = csvData['rangeband']
            outputRecord['system']['weaponType'] = csvData['weapontype']
            outputRecord['system']['damageType'] = csvData['damagetype']
            outputRecord['system']['rateOfFire'] = csvData['rateoffire']
            if csvData['recoil'] == "TRUE":
                outputRecord['system']['recoil'] = True
            else:
                outputRecord['system']['recoil'] = False
            outputRecord['system']['armorPiercing'] = int(csvData['armorpen'])
            outputRecord['system']['handlingModifiers'] = csvData['handlingmod']
        else:
            print(f"{type} type not yet supported")
    return (outputRecord, folders)

def processType(type:str, outFile, inFile):
    dictFolders = {}
    dbOutput = []
    print(f"Start processing {type} file {inFile.name}")
    with open(inFile, newline='') as csvfile:
        csvInput = csv.DictReader(csvfile)
        for row in csvInput:
            (recordtoWrite, dictFolders) = makeOutputRecord(row, type, dictFolders)
            dbOutput.append(json.dumps(recordtoWrite))
    # output the folder lines
    for dir in dictFolders:
        dbOutput.append(json.dumps(dictFolders[dir]))
    firstLine = True
    with open(outFile, 'w') as dbFile:
        for rec in dbOutput:
            if firstLine:
                dbFile.write(rec)
                firstLine = False
            else:
                dbFile.write("\n"+rec)
    print(f"Complete processing {type} file {inFile.name}")
    return True

def main ():
    inputFolder = "input"
    outputFolder = "output"
    weaponFile = "weapon"
    armorFile = "armor"
    itemFile = "item"
    ammoFile = "ammo"
    inputSuffix = ".csv"
    outputSuffix = ".db"
    foundryPrefix = "mtg2-"

    inputPath = Path('./'+inputFolder)
    listInputFiles = list(inputPath.glob('*'+inputSuffix))
    for f in listInputFiles:
        if f.name == armorFile+inputSuffix:
            # process as armor
            processType('armor', Path(outputFolder, foundryPrefix+armorFile+outputSuffix), f)
        if f.name == weaponFile+inputSuffix:
            # process as wepon
            processType('weapon', Path(outputFolder, foundryPrefix+weaponFile+outputSuffix), f)
        if f.name == itemFile+inputSuffix:
            # process as item
            print(f"Start processing item file {f.name}")
        if f.name == ammoFile+inputSuffix:
            # process as ammo
            print(f"Start processing ammo file {f.name}")
    return True

if __name__ == "__main__":
    main()
