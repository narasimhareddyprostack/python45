import json 
emp_dict={'id': 1,
          'name': 'rajni', 
          'email': 'rajni@jailer.com', 
          'gender': 'Male', 
          'avail': True, 
          'discout': None
          }

fp=open('new_emp.json','w')
json.dump(emp_dict,fp)


fp.close()