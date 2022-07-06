# PYTHON ATM PROGRAM BY PYTHONDEX
# Visit https://pythondex.com for more information.

from datetime import date
date = date.today()
#name = input ("Please enter your name: ")
print ("Hello", "Todays date is", date)
user = {
    'pin': 1234,
    'pin': 9876,
    'balance':1000
}

def widthdraw_cash():
    while True:
        amount = int(input("**Enter the amount of money you want to widthdraw**: "))
        if amount > user['balance']:
            print("You don't have sufficient balance to make this widthdrawal")
        else:
            user['balance'] = user['balance'] - amount
            print("Withdrawing.....................................")
            print("................................................0%")
            print("................................................10%")
            print("................................................20%")
            print("................................................30%")
            print("................................................40%")
            print("................................................50%")
            print("................................................60%")
            print("................................................70%")
            print("................................................80%")
            print("................................................90%")
            print("................................................100%")

            print(f"{amount} Dollars successfully widthdrawn your remaining balance is {user['balance']} Dollars")
            print('')
            return False

def balance_enquiry():
    print("****************************************")
    print("########################################")
    print(f"Total balance {user['balance']} Dollars")
    print('')


is_quit = False

print('')
print("Welcome to the Sator ATM")

pin = int(input('Please enter your four digit pin: '))

if pin == user['pin']:
    while is_quit == False:
        print("what do you want to do")
        print(" Enter 1 to Widthdraw Cash \n Enter 2 for Balance Enquiry \n Enter 3 to Quit")

        query = int(input("Enter the number corresponding to the activity you want to do: "))

        if query == 1:
            widthdraw_cash()
        elif query == 2:
            balance_enquiry()
        elif query == 3:
            is_quit = True

        else:
            print("Please enter a correct value shown")
else:
    print("Entered wrong pin")
