
try:
    print(int("Hello"))

except (ValueError, ZeroDivisionError, NameError, AttributeError) as err:
    print(err)
