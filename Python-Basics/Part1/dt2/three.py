#read data from command line arguments 
#print sum/total of command line arguments
#py three.py  10 20 30 40 50 60 70 80
#output - 100 

from sys import argv 
a = int(argv[1])
b = int(argv[2])
c = int(argv[3])
d = int(argv[4])

print(a+b+c+d)