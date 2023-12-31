
def deposit():
    while True:
        amount = input("What is the amount? $")
        if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    break
                else:
                    print("Amount must be greater than 0")
        else:
            print("Enter an Amount")
    return  amount
#deposit()
def withdraw():

