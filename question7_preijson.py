import json
dict1={}
with open("pre.text","r") as f:
    for i in f:
        key,value=i.strip().split(None,1)
        dict1[key]=value.strip()
outfile=open("o.json","w")
json.dump(dict1,outfile,indent=4)
print(json.dumps(dict1,indent=4))
outfile.close