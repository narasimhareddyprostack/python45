# KA04MM8798
# KA 04 AA 7977
from re import fullmatch
regno = input("Enter your vehicle Number::::")
match = fullmatch('KA[0-9]{2}[A-Z]{2}[0-9]{4}', regno)

if match != None:
    print("Given Reg is Valid ")
else:
    print("Not Valid")
