a=100
b=200
def f1():
    c=300
    print(a)  #100
    print(b)  #200
    print(c)  #300
def f2():
    print(a)  #100
    print(b)  #200
    print(c)  #NameError

f1()
f2()