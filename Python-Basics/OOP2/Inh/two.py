class Account:
    def open_account(self):
        print("Account class - open Account method")

    def get_detials(self):
        print("Getting Details")


class SA(Account):
    def cal_bal(self):
        print("Your Bal is Zero")


class CA(Account):
    def cal_bal(self):
        print("Your Bal is Netagive Bal")


sa1 = SA()
ca1 = CA()

sa1.open_account()
sa1.get_detials()
sa1.cal_bal()


ca1.open_account()
ca1.get_detials()
ca1.cal_bal()
