# Remove Duplicates from a List

total_elements = int(input("Enter number of elements: "))

my_list = []

for index in range(total_elements):
    number = int(input("Enter a number: "))
    my_list.append(number)

unique_list = []

for number in my_list:
    if number not in unique_list:
        unique_list.append(number)

print("Original list:", my_list)
print("List after removing duplicates:", unique_list)