
def showBalance(balance):
    print(f"Your balance is: {balance}")

def deposit():
    amount = int(input("How much would you like to deposit: "))

    if amount < 0:
        print("Can't deposit negative numbers!")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = int(input("How much would you like to withdraw: "))
    
    if amount > balance:
        print("Insufficient funds to withdraw")
        return 0

    if amount < 0:
        print("Can't withdraw negative numbers!")
        return 0
    
    else:        
        print(f"Succesfully withdrawn {amount}")
        return amount    

def main():

    balance = 0
    isRunning = True

    while isRunning:
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter (1-4): ")

        match choice:
            case '1':
                showBalance(balance)

            case '2':
               balance += deposit()

            case '3':
             balance -= withdraw(balance)

            case '4':
                isRunning = False

            case _:
                print("Not a valid input")                
        print()        

if __name__ == '__main__':
    main()        