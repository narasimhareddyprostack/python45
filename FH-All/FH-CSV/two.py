#read csv file - data.csv 

import csv 
fp=open('data.csv','r')
csv_reader_obj=csv.reader(fp)

for line in csv_reader_obj:
    print(line)
    
""" print(csv_reader_obj)
print(type(csv_reader_obj)) """

fp.close()