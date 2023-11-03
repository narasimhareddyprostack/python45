class Account:

    def open_account(self):
        print('account opened successfully')
    
    def deposit_amount(self,amount):
        print("Amount deposited",amount)
    

a1=Account()
a1.open_account()
a1.deposit_amount(3000)