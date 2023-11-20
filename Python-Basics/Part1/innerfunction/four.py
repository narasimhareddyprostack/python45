def outer():
    print("***Outer Function***")

    def inner():
        print('****Inner Function***')
    

    return inner


inner=outer()
inner()
inner()
inner()
