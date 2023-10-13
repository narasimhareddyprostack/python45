#read 3 three number from keyboard and print min and max

a,b,c=input("Enter Number:::").split(" ")
print(a)
print(b)
print(c)

if a < b and a < c:
    print("Min value is:", a)
elif b < c:
    print("Min value:", b)
else:
    print("Min value:", c)
