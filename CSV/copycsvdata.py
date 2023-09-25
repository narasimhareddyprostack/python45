import csv
f1 =open('emp.csv','r')
f2 =open('temp.csv', 'w')
fp1 =csv.reader(f1)
fp2 = csv.writer(f2)

for data in fp1:
    fp2.writerow(data)

f1.close()
f2.close()