class Parent1:
    def m1(self):
        print("Parent1 - class m1 method")

    def m2(self):
        print("Parent1 - class m2 method")


class Parent2:
    def m3(self):
        print("Parent2 - class m3 method")


class Child(Parent1, Parent2):
    def m4(self):
        print("Child - class m4 method")


c1 = Child()
c1.m1()
c1.m2()
c1.m3()
c1.m4()
