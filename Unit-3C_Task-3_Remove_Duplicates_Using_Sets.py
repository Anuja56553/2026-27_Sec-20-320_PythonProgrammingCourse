# Remove Duplicates Using Sets

total_elements = int(input("Enter number of elements: "))

my_list = []

for index in range(total_elements):
    number = int(input("Enter a number: "))
    my_list.append(number)

print("Original List:", my_list)

unique_set = set(my_list)

unique_list = list(unique_set)

print("List after removing duplicates:", unique_list)