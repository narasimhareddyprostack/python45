from Errors import InsuffientFundsError
acc_bal = 300


def withdrawl(amount):

    if acc_bal < amount:
        raise InsuffientFundsError("No Funds! Try Later")
    else:
        print("Enjoy")


withdrawl(500)
