#print all students
import json 

fp=open('student.json','r')
students=json.load(fp)

for student in students:
    print(student['name'])