def login_req(func):
    def inner(name,flag):
        if flag == False:
            print("Login Required")
        else:
            return func(name,flag)
    return inner


def home_page(name,flag):
    print('Home Page')


@login_req
def order_page(name, flag):
    print('Order Page')



def payment_page(name, flag):
    print('Payment Page')

home_page('rahul',True)
order_page('rahul',True)
payment_page('rahul',False)
