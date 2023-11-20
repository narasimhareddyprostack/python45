#read csv file - data.csv 

import csv 
fp=open('data.csv','r')
csv_reader_obj=csv.reader(fp)

print(csv_reader_obj)
print(type(csv_reader_obj))

for line in csv_reader_obj:
    for word in line:
        print(word,end="\t")
    print()

fp.close()