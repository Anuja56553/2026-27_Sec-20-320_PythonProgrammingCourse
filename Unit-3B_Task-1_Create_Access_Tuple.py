# Create and Access a Tuple

total_elements = int(input("Enter number of elements: "))

my_tuple = ()

for index in range(total_elements):
    element = input("Enter an element: ")
    my_tuple = my_tuple + (element,)

print("Tuple:", my_tuple)

print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

print("Length:",len(my_tuple))
