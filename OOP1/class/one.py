class Account:
    min_bal=500

    def open_account(self):
        self.a=10
        self.b=20

    def deposit_amount(self):
        pass 

    def get_bal(self):
        pass 

a1=Account()
a2=Account()

print(a1)
a1.open_account()
print(a1.__dict__)

print(a2)
print(a2.__dict__)

