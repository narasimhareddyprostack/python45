class Account:
    min_bal = 500  # static variable
    noofObj = 0    # static variable

    def __init__(self, id, name):
        self.acc_id = id
        self.acc_name = name
        self.acc_bal = 0
        Account.noofObj = Account.noofObj + 1

    def set_accBal(self, amount):
        self.acc_bal = self.acc_bal + amount

    @classmethod
    def update_minBal(cls):
        cls.min_bal = 600

    @staticmethod
    def cal_Tax():
        return 10

    @classmethod
    def get_noOfObjs(cls):
        return cls.noofObj


a1 = Account(101, 'Rahul')
a2 = Account(102, 'Sonia')
a3 = Account(103, 'Priyanka')
a4 = Account(104, 'Modi')
a5 = Account(104, 'Suhail')

Account.update_minBal()

print(a1.min_bal)
print(a2.min_bal)
print(Account.min_bal)

print(Account.cal_Tax())


print("No of Acccounts:", Account.get_noOfObjs())
