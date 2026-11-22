# Set Creation and Basic Set Operations

first_set = set(input("Enter first set elements: ").split())
second_set = set(input("Enter second set elements: ").split())

print("First Set:", first_set)
print("Second Set:", second_set)

# Union
print("Union:", first_set | second_set)

# Intersection
print("Intersection:", first_set & second_set)

# Difference
print("Difference:", first_set - second_set)