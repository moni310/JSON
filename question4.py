import json
data={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
print(data)
print("  ")
print("json_data")
data1=json.dumps(data, sort_keys=True ,indent=4)
print(data1)




