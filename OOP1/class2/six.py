class Account:
    
    def __init__(self,id,name):
        self.acc_id=id
        self.acc_name=name




a1=Account(101,'Rahul')
a2=Account(102,'sonia')
print(a1.__dict__)
print(a2.__dict__)