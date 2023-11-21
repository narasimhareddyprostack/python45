
import re
mno = input("Enter Mobile Number::::")

match = re.fullmatch('[6-9]\d{9}', mno)

if match != None:
    print("Valid Mobile Number")
else:
    print("Not a Valid Number")
