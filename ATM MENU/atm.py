# Simple ATM Simulation

balance = 1000
pin = "1234"


def check_balance():
    print("Your balance is:", balance)


def deposit():
    global balance

    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        balance += amount
        print("Deposit successful!")
        print("New balance:", balance)
    else:
        print("Invalid amount.")


def withdraw():
    global balance

    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("Withdrawal successful!")
        print("New balance:", balance)


def change_pin():
    global pin

    old_pin = input("Enter your current PIN: ")

    if old_pin == pin:
        new_pin = input("Enter your new PIN: ")
        pin = new_pin
        print("PIN changed successfully!")
    else:
        print("Incorrect PIN.")


# Login
entered_pin = input("Enter your PIN: ")

if entered_pin == pin:

    # ATM menu loop
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            change_pin()

        elif choice == "5":
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Incorrect PIN. Access denied.")
