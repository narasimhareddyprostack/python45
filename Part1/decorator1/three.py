def outer():
    print("Outer Function")
    def inner():
        print("Inner Function")

    inner()
    inner()


outer()
inner()