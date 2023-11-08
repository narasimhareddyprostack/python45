from Errors import InsuffientFundsError
acc_bal = 1300


def withdrawl(amount):

    if acc_bal < amount:
        try:
            raise InsuffientFundsError("No Funds! Try Later")
        except InsuffientFundsError as err:
            print(err)

    else:
        print("Enjoy")


withdrawl(500)
