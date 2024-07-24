def show_balance():
    print(f"Your Balance is ${balance:.2f}")

def deposite():
    amount = float(input("Enter an Amount to be deposited: "))
    print("Deposite Sucessfully ✅")

    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
      return amount
def withdraw():
    amount = float(input("Enter amount to be withdraw: "))
    print("Withdraw Sucessfully ✅")

    if amount > balance:
        print("Insufficient Funds")
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

balance = 0
is_running = True

while is_running:
    print("------------------------")
    print("    Banking Program     ")
    print("------------------------")

    print("1. Show Balance")
    print("------------------------")

    print("2. Deposite")
    print("------------------------")

    print("3. Withdraw")
    print("------------------------")

    print("4. Exit")
    print("------------------------")


    choice = input("Enter Your Choice (1-4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposite()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("This is not a vaild choice")
        print("------------------------")

        print("Thankyou Have a Nice Day!")

