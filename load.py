import json
f=open("data.json","r")
data=json.load(f)
print(data)
f.close