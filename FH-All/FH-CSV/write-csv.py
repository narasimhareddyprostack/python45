import csv 

fp=open('user.csv','w',newline="")
csv_obj=csv.writer(fp)

csv_obj.writerow(['uid','uname','uemail'])
csv_obj.writerow([11,'rahul','rahul@gmail.com'])
csv_obj.writerow([12,'rahul','rahul@gmail.com'])
csv_obj.writerow([13,'rahul','rahul@gmail.com'])
csv_obj.writerow([14,'rahul','rahul@gmail.com'])

fp.close()