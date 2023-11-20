class Account:
    def __init__(self):
        print("Account - class constructor")


class SA(Account):
    def __init__(self):
        super().__init__()
        print("SA - class constructor")


SA()
