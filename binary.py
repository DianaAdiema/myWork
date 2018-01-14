from datetime import datetime

transaction_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
balance = 0

print("Welcome to Hala Bank\n")

print("Kindly enter your pin to proceed: ")
pin = input()


if (pin == '1234'):
    print("You can perform the following operations:\n")
    print("1. Deposit\n")
    print("2. Withdraw\n")
    print("3. Check Balance\n")
    print("4. Change Pin\n")
    choice=input()
    while choice == '1':
        print("Enter the amount to deposit: ")
        deposit = input()
        if int(deposit)<50:
            print("The minimum deposit amount is 50. Select 1 to try again")
        else:
            balance = +int(deposit)
            print("Deposit successfull at", transaction_time)
    while choice == '2':
        print("Enter the amount to Withdraw: ")
        to_withdraw = input()
        if (int(to_withdraw)<50):
            print("The minimum amount to Withdraw is 50. Select 2 to try again")
        else:
            balance = -to_withdraw
            print("Withdrawal successfull at", transaction_time)
    while choice == '3':
        print("Your account balance is: ", balance)
    while choice == '4':
        print("Please enter your current pin: ")
        pin= input()
        if pin == '1234':
            print("Please enter your new pin: ")
            new_pin = input()
            print("Please confirm your new Pin")
            new_pin2 = input()
            if new_pin == new_pin2 :
                print("Your pin has been reset")
            else:
                print("Select 4 to try again")
        else:
            print("You have input the wrong pin")
else:
    print("You have input the wrong pin")







