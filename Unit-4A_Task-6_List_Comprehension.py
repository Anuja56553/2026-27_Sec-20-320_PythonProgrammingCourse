n = int(input("Enter a number: "))

squares = [x*x for x in range(1, n+1)]
even_numbers = [x for x in range(1, n+1) if x % 2 == 0]

print("Squares:", squares)
print("Even Numbers:", even_numbers)
