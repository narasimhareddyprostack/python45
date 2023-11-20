class Test:
    def m1(self, arg1):
        print(arg1)

    def m1(self, arg1, arg2):
        print(arg1)

    def m1(self, arg1, arg2, arg3):
        print(arg1)


Test().m1(10,20,30)
