#read 3 number from keybords and print min value and max value

a = int(input("Enter First Number:"))
b = int(input("Enter First Number:"))
c = int(input("Enter First Number:"))

if a<b and a<c:
    print("Min value is:", a)
elif b<c:
    print("Min value:", b)
else:
    print("Min value:",c)