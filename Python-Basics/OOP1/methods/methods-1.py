class Account:
    min_bal = 500  # static variable

    def __init__(self, id, name):
        self.acc_id = id
        self.acc_name = name
        self.acc_bal = 0

    def set_accBal(self, amount):
        self.acc_bal = self.acc_bal + amount


a1 = Account(101, 'Rahul')
a2 = Account(102, 'Sonia')
print(a1.__dict__)
print(a2.__dict__)

a1.set_accBal(67000)
a1.set_accBal(67000)
print(a1.__dict__)
print(a2.__dict__)
