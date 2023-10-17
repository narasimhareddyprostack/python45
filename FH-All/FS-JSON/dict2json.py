import json 
emp_dict={'eid': 101, 
           'ename': 'rahul Gandhi', 
           'esal': 45000, 
           'avail': True, 
           'city': None
           }
#dict2json  - dumps
emp_json_str=json.dumps(emp_dict)
print(emp_dict)
print(emp_json_str)