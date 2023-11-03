class Test:
    def __init__(self, value):
        self.a = value

    def m1(self):
        self.b = 200

    @classmethod
    def m2(cls):
        cls.c = 300

    @staticmethod
    def m3():
        # self.d = 400
        # cls.e = 500
        Test.f = 600


t1 = Test(100)

print(t1.__dict__)
t1.m1()
print(t1.__dict__)

Test.m2()
print(t1.__dict__)
print(Test.__dict__)

Test.m3()
print(Test.__dict__)


print(t1.__dict__)
print(Test.__dict__)
