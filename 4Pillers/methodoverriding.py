class A:
    def m1(self):
        print("class A - m1 method")


class B(A):
    pass
    """ def m1(self):
        print("class B - m1 method") """


obj = B()
obj.m1()
