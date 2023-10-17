#read user data from keyboard and write in to csv 
import csv

fp=open('userdata.csv','w',newline="")
csv_obj=csv.writer(fp)
csv_obj.writerow(['name','email','city'])

no_users=int(input("Enter No of users:"))

for x in range(no_users):
    name = input("Enter User Name:")
    email = input("Enter User Email :")
    city = input("Enter User City :")
    csv_obj.writerow([name,email,city])

fp.close()