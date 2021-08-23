import json

JSON_FILE = "./data.json"

def Find_Index(_list, id):
    for i in _list:
        if i["id"] == id:
            return i
    return "data don't here"

with open(JSON_FILE,'r') as rf:
    data = json.load(rf)

    INP = input("Enter Your ID:")
    Your_data = Find_Index(data["Bio"],INP)
    print(Your_data)
    key_list = []
    for i in Your_data.keys():
        if i != "id":
            key_list.append(i)
    print("Which Information do you want to update ? {}".format(" >>".join(key_list)))  
    INP_KEY = input("Enter That here::")
    INP_VALUE = input("Enter Update Value::")
    Your_data[INP_KEY] = INP_VALUE 
    
with open(JSON_FILE,"w") as fw:
    json.dump(data,fw)




