def outer():
    pass
    def inner():
        pass
    
    print(id(inner))
    return inner

rajni = outer()
print(id(rajni))
