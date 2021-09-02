import json
lis=[3,5,2,"moni"]
data=open("file.json","w")
json.dump(lis,data,indent=4)
print(data)
data.close()