# List Operations

total_elements = int(input("Enter number of elements: "))

my_list = []

for index in range(total_elements):
    number = int(input("Enter a number: "))
    my_list.append(number)

print("Original list:", my_list)

insert_number = int(input("Enter number to insert: "))
insert_position = int(input("Enter position to insert: "))
my_list.insert(insert_position, insert_number)
print("After insert:", my_list)

append_number = int(input("Enter number to append: "))
my_list.append(append_number)
print("After append:", my_list)

remove_number = int(input("Enter number to remove: "))
if remove_number in my_list:
    my_list.remove(remove_number)
    print("After remove:", my_list)
else:
    print("Number not found")

my_list.sort()
print("After sorting:", my_list)

my_list.reverse()
print("After reversing:", my_list)