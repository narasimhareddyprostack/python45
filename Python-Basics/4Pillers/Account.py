# from Bank import Bank
from Bank import *


class Account(Bank):

    def __init__(self, name, email, address):
        self.acc_name = name
        self.acc_email = email
        self.acc_address = address

    def cal_bal(self):
        pass

    def open_account(self):
        print('account opened successfully')

    def set_mobile_no(self, no):
        self.acc_mobile = no

    def get_mobile_no(self):
        return self.acc_mobile


""" a1 = Account('rahul', 'rahul@gmail.com', 'Bangalore')

print(a1.__dict__)
a1.open_account()
a1.set_mobile_no(9591)
print(a1.get_mobile_no()) """
