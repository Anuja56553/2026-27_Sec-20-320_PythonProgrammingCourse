balance = 1000

def deposit():
    global balance
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    print("Updated balance:", balance)

def show_local_balance():
    balance = int(input("Enter local balance: "))
    print("Local balance:", balance)

print("Initial balance:", balance)

deposit()
show_local_balance()

print("Final bank balance:", balance)