class Account:

    def open_account(self):
        print('account opened successfully')
    
    def deposit_amount(self):
        print("Amount deposited")
    
    def withdrawl(self):
        print("Insufficent Bal")
    
    def get_bal(self):
        return 100

a1=Account()
a1.open_account()
a1.deposit_amount()
a1.withdrawl()
print(a1.get_bal())