# Maximum and Minimum in a Tuple

total_elements = int(input("Enter number of elements: "))

my_list = []

for index in range(total_elements):
    number = int(input("Enter a number: "))
    my_list.append(number)

my_tuple = tuple(my_list)

if total_elements > 0:
    print("Tuple:", my_tuple)
    print("Maximum element:", max(my_tuple))
    print("Minimum element:", min(my_tuple))
else:
    print("Tuple is empty")