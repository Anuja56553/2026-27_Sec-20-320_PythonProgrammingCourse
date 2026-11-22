balance = 1000

def show_balance():
    balance = int(input("Enter local balance: "))
    print("Local balance:", balance)

print("Global balance:", balance)
show_balance()
print("Global balance after function:", balance)
