import json
JSON_FILE ='./data.json'

def Find_Index(_list, id):
    for i in _list:
        if i["id"] == id:
            return i
    return "data don't here"

with open(JSON_FILE,'r') as fr:
    data = json.load(fr)
    INP = input("Enter your ID:")
    Value = Find_Index(data["Bio"],INP)
    print(Value)
