# Create, Traverse and Display a List

total_elements = int(input("Enter number of elements: "))

my_list = []

for index in range(total_elements):
    element = input("Enter an element: ")
    my_list.append(element)

print("List elements are:")

for element in my_list:
    print(element)