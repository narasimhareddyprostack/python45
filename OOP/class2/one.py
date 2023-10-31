class Account:

    def open_account(self):
        print('account opened successfully')
    
    def deposit_amount(self):
        print("Amount deposited")
    
    def withdrawl(self):
        print("Insufficent Bal")
    
    def get_bal(self):
        return 0

a1=Account()
a2=Account()
print(a1)
print(id(a1))
print(a1.__dict__)
     