def outer():
    print("***Outer Function***")

    def inner():
        print('****Inner Function***')
    

    return 100


x=outer()
print(x)