# Tuple Operations

first_tuple = tuple(input("Enter first tuple elements: ").split())
second_tuple = tuple(input("Enter second tuple elements: ").split())

# Concatenation
combined_tuple = first_tuple + second_tuple
print("Concatenation:", combined_tuple)

# Slicing
print("Slicing:", combined_tuple[0:3])

# Unpacking
first_value, second_value, *remaining_values = combined_tuple

print("First value:", first_value)
print("Second value:", second_value)
print("Remaining values:", remaining_values)