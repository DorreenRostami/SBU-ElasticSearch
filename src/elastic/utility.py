import csv
import json
from datetime import datetime
from pathlib import Path
import re


class CsvToJson:
    def convert(self):
        csvPath = "data/QueryResults.csv"
        jsonPath = "data/QueryResults.json"
        data = []
        with open(csvPath) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                # id = rows['Id']
                data.append(rows)

        # create new json File and Write data on it
        with open(jsonPath, 'w') as jsonFile:
            # make it more readable and pretty
            jsonFile.write(json.dumps(data, indent=4))

    @classmethod
    def convertToArray(cls, csvFilePath):
        csvPath = csvFilePath
        # jsonPath="data/QueryResults.json"
        data = []
        with open(csvPath) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                # id = rows['Id']
                data.append(rows)
        return data

    @classmethod
    def convertToArrayDictionary(cls, jsonPath):
        data = []
        with open(jsonPath.absolute()) as f:
            data = json.load(f)
        return data

    @classmethod
    def convertScoreStringToint(cls, jsonPath):
        data = []
        with open(jsonPath) as f:
            data = json.load(f)
            for d in data:
                d['Score'] = int(d['Score'])

        with open(jsonPath, 'w') as jsonFile:
            # make it more readable and pretty
            jsonFile.write(json.dumps(data, indent=4))

    @classmethod
    def convertParentIdStringToInt(cls, jsonPath):
        data = []
        with open(jsonPath) as f:
            data = json.load(f)
            for d in data:
                d['ParentId'] = int(d['ParentId'])

        with open(jsonPath, 'w') as jsonFile:
            # make it more readable and pretty
            jsonFile.write(json.dumps(data, indent=4))

    @classmethod
    def convertCreationDateStringToInt(cls, jsonPath):
        data = []
        with open(jsonPath) as f:
            data = json.load(f)
            for d in data:
                d['CreationDate'] = int(datetime.strptime(
                    d['CreationDate'], '%Y-%m-%d %H:%M:%S').utcnow().timestamp()) * 1000

        with open(jsonPath, 'w') as jsonFile:
            # make it more readable and pretty
            jsonFile.write(json.dumps(data, indent=4))

    @classmethod
    def convertCreationDateStringTomilisecond(cls, jsonPath):
        data = []
        with open(jsonPath) as f:
            data = json.load(f)
            for d in data:
                d['CreationDate'] = d['CreationDate'] * 1000

        with open(jsonPath, 'w') as jsonFile:
            # make it more readable and pretty
            jsonFile.write(json.dumps(data, indent=4))


def saveToJsonFile(data, dir_Path):
    # create new json File and Write data on it
    with open(Path(dir_Path).absolute(), 'w', encoding='utf-8') as jsonFile:
        # make it more readable and pretty
        jsonFile.write(json.dumps(data, indent=4, ensure_ascii=False))


def loadFromJsonFile(file_Path):
    data = []
    with open(Path(file_Path).absolute()) as f:
        data = json.load(f)
    return data


def removeTabAndLineCharacter():
    pass


# it removes \t and \n and spaces
def removeTabAndLineCharacterAndSpaces(input):
    return re.sub(r'\s+', '', input)


def removeHTMLTags(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def persianCharacterResolver(per_string):
    switcher = {
        "۰": "0",
        "۱": "1",
        "۲": "2",
        "۳": "3",
        "۴": "4",
        "۵": "5",
        "۶": "6",
        "۷": "7",
        "۸": "8",
        "۹": "9"}

    resolved_string = ""
    for per_char in per_string:
        resolved_string += switcher.get(per_char, "")

    return int(resolved_string)


def checkForNone(input):
    if (input is None):
        return NoneVal()
    else:
        return input


class NoneVal:
    def get_text(self):
        return "None"


def convertToArrayDictionary(jsonPath):
    data = []
    with open(jsonPath.absolute(), encoding="utf-8") as f:
        data = json.load(f)
    return data
