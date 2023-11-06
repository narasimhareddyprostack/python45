from Account import *


class CA(Account):
    min_bal = 25000

    def __init__(self, id, name, email, address, amout):
        super().__init__(name, email, address)
        self.acc_id = id
        self.acc_bal = amout

    def cal_bal(self):
        return self.acc_bal - self.min_bal


ca1 = CA(201, 'rajni', 'rajil@gmail.com', 'chennai', 80000)

""" print(ca1.cal_bal()) """
""" 
print(ca1.__dict__)
ca1.open_account()
ca1.set_mobile_no(9898099808)
print(ca1.get_mobile_no())
 """
