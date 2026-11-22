# Set Membership Testing and Methods

my_set = set(input("Enter set elements: ").split())

print("Original Set:", my_set)

search_element = input("Enter element to search: ")

if search_element in my_set:
    print("Element is present")
else:
    print("Element is not present")

# Add
add_element = input("Enter element to add: ")
my_set.add(add_element)
print("After add:", my_set)

# Remove
remove_element = input("Enter element to remove: ")

if remove_element in my_set:
    my_set.remove(remove_element)
    print("After remove:", my_set)
else:
    print("Element not found")

# Discard
discard_element = input("Enter element to discard: ")
my_set.discard(discard_element)
print("After discard:", my_set)