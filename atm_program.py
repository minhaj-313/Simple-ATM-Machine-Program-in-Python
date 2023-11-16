def check_balance():
    print("Your Current Balance is:", balance, "Rupees only")

def deposit():
    global balance
    damount = int(input("Enter your Deposit amount: "))
    balance += damount
    print("Successfully Deposited")

def withdraw():
    global balance
    amount = int(input("Enter the Withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        print("Transaction Successful")
    else:
        print("Insufficient Balance")

def main():
    pin = 1234
    balance = 1000000
    
    print('Insert your Card')
    confirm_pin = int(input("Enter Your Pin: "))

    if pin == confirm_pin:
        print("Enter 1 for Balance Inquiry")
        print("Enter 2 for Money Withdrawal")
        print("Enter 3 for Money Deposit")
        
        option = int(input("Select an option (1/2/3): "))

        if option == 1:
            check_balance()
        elif option == 2:
            withdraw()
        elif option == 3:
            deposit()
        else:
            print("Invalid Option")
    else:
        print("Invalid PIN")

    print("Thank You, Visit Again")


if __name__ == "__main__":
    main()
