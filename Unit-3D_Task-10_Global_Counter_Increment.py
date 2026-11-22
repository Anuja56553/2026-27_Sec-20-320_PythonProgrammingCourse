counter = 0

def increment():
    global counter
    counter = counter + 1
    print("Counter:", counter)

n = int(input("Enter how many times to increment: "))

for i in range(n):
    increment()