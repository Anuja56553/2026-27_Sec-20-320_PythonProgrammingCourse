# Simple Interest Using Default Arguments

def simple_interest(principal, time, rate=5):
    interest = (principal * time * rate) / 100
    return interest

principal = float(input("Enter principal amount: "))
time = float(input("Enter time in years: "))

# Calling with default rate
interest1 = simple_interest(principal, time)
print("Simple Interest with default rate (5%):", interest1)

# Calling with user-given rate
rate = float(input("Enter another rate: "))
interest2 = simple_interest(principal, time, rate)
print("Simple Interest with given rate:", interest2)