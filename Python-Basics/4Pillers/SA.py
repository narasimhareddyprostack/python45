from Account import *


class SA(Account):
    min_bal = 500   # static variable

    def __init__(self, id, name, email, address, amount):
        super().__init__(name, email, address)
        self.acc_id = id
        self.acc_bal = amount

    def cal_bal(self):
        return self.acc_bal - self.min_bal


sa1 = SA(101, 'rahul', 'rahul@gmail.com', 'Bangalore', 5000)
sa2 = SA(102, 'sonia', 'sonia@gmail.com', 'New Delhi', 50000)


""" print(sa1.cal_bal())
print(sa2.cal_bal()) """
""" print(sa1.__dict__)
print(sa2.__dict__)

sa1.open_account()
sa1.set_mobile_no(9591)
print(sa1.get_mobile_no())
sa2.open_account()
sa2.set_mobile_no(54545)

print(sa1.get_mobile_no())


print(sa1.__dict__)
print(sa2.__dict__)
 """
