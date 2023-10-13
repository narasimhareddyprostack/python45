a=100
b=200
def f1():
    c=300
    global d
    d=400
    print(a)  #100
    print(b)  #200
    print(c)  #300
    print(d)  #400
def f2():
    print(a)  #100
    print(b)  #200
    #print(c)  #NameError
    print(d)  #NameError

f1()
f2()