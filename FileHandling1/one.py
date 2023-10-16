#read data.txt file, print data in terminal
fp=open('data.txt','r')

#data1=fp.read()
#data=fp.read(10)
data = fp.readlines()
print(data)

for line in data:
    print(line)

fp.close()
