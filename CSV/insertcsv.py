import csv
field=["eid","ename","esal"]
f = open('emp.csv', 'w')
fp=csv.writer(f)
fp.writerow(field)
ch='y'
while ch=='y' or ch=='Y':
    eid=int(input("Enter Emp Id:"))
    ename=input("Enter Emp Name:")
    esal=input("Enter Emp Salary:")
    fp.writerow([eid,ename,esal])
    ch = input("Wanna! more emp reocr? y/n::::")
f.close()