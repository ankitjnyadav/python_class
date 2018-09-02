import json
my_data=["Hafsa Jabeen","Reading and writing files in python",78546]
json.dumps(my_data)
with open("jsonfile.json","w") as f:
    json.dump(my_data,f)
f.close()
with open("jsonfile.json","r") as f:
    jsondata=json.load(f)
    print(jsondata)
f.close()