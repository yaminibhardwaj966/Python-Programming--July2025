import json 

details={"id":101,"name":"yamini","address":"aligarh"}

print(json.dumps(details,indent=4))
print(json.loads(details))
print(details["id"])