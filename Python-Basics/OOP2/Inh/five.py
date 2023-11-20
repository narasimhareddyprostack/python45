class Parent1:
    def m1(self):
        print("Parent1 - class m1 method")

    def m2(self):
        print("Parent1 - class m2 method")


class Parent2:
    def m1(self):
        print("Parent2 - class m1 method")


class Parent3:
    def m1(self):
        print("Parent3 - class m1 method")


class Child(Parent1, Parent2, Parent3):
    def m4(self):
        print("Child - class m4 method")


c1 = Child()

c1.m1()
