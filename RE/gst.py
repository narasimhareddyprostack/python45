import re


gstno = input("Enter GST Number")
match = re.fullmatch(
    '^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$', gstno)
if match != None:
    print('Given GST is valid')
else:
    print("Go To Hell")
