def login_req(func):
    def inner(name,flag):
        if flag == False:
            print("Login Required")
        else:
            return func(name,flag)
    return inner

@login_req
def home_page(name,flag):
    print('Home Page')


@login_req
def order_page(name, flag):
    print('Order Page')


@login_req
def payment_page(name, flag):
    print('Payment Page')

home_page('rahul',False)

order_page('rahul',True)
payment_page('rahul',False) 
