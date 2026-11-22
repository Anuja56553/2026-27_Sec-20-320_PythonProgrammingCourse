from functools import reduce

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Using map()
square = list(map(lambda x: x * x, numbers))
print("Squares:", square)

# Using filter()
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

# Using reduce()
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)