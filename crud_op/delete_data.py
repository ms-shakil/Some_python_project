
import json
JSON_FILE ='./data.json'

def Find_Index(_list, id):
    for i in _list:
        if i["id"] == id:
            return i
    return "data don't here"

with open(JSON_FILE, "r") as fr:
    data = json.load(fr)
    INP = input("Enter Yor ID:")
    value = Find_Index(data["Bio"],INP) 
    data["Bio"].remove(value)

    data["Total"] = len(data["Bio"])

    dicts = {}
    arr = []
    for i in data["Bio"]:
        dic = i["district"]
        if dic in dicts:
            dicts[dic] +=1
        else:
            dicts[dic] =1    
    for name ,count in dicts.items():
        arr.append({
            "name":name,
            "count": count
        })

    data["Districts"]  = arr    
with open(JSON_FILE,'w') as fw:
    json.dump(data,fw)       