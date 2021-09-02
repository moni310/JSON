import json
data=[8,"aj",6+7j]
file=open("my_file1.json","w")
json.dump(data,file,indent=4)
print(file)
file.close

# we can not convert complex data type python to json.