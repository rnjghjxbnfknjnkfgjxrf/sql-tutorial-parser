from sql_tutorial_parser import SqlTutorialParser
import json

parser = SqlTutorialParser()
result = parser.parse()
with open('result.json', 'w') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)