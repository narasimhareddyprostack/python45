import json 

fp=open('emp.json','r')
emp_dict=json.load(fp)

print(emp_dict)
fp.close()