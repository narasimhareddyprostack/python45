import json 
emp_JSON_String='''{
    "eid":101,
    "ename":"rahul Gandhi",
    "esal":45000,
    "avail":true,
    "city":null

}'''

emp_dict=json.loads(emp_JSON_String)
print(emp_dict)

print(emp_dict['ename'])