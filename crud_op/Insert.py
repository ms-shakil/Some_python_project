import json
JSON_FILE ="./data.json"

def Valid_Id(Arr,id):
    found = False
    for i in Arr:
        if i["id"] == id :
            found = True
            return found
    return found

with open(JSON_FILE,'r') as fd:
    data = json.load(fd)

    print("There are {} in this file".format(len(data["Bio"])) )
    INP = int(input("How many Students data do you want insert?:"))
    i = 0
    while  i < INP:
        student = {
            "id":input("Enter ID:"),
            "name": input("Enter Name:"),
            "age":input("Enter Age:"),
            "district": input("Enter District Name:").upper()
        }
        if Valid_Id(data["Bio"],student["id"]):
            print("This id already exist")
        else:
            data["Bio"].append(student)    
            i+=1
    data["Total"] = len(data["Bio"])

    My_dic ={}
    My_arr =[]
    for i in data["Bio"]:
        dic = i["district"]
        if dic in My_dic:
           My_dic[dic] +=1
        else:
            My_dic[dic] =1
    
    for name,count in  My_dic.items():
        My_arr.append({
            "name":name,
            "count":count
        })

    data["Districts"]    = My_arr   

with open(JSON_FILE,"w")  as ff:
    json.dump(data,ff)           
