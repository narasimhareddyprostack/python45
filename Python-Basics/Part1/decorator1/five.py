def division_logic(func):

    def inner(a,b):
        if b==0:
            print("can't divide by Zero")
        else:
            return func(a,b)

    return inner

@division_logic
def divide(a,b):
    print(a/b)



divide(10,5)
divide(10,0)