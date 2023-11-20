try:
    num1 = int(input("Enter First Number:"))
except ValueError as err:
    print(err)
    num1 = 0


print("GM")
print(num1)
print("GN")
