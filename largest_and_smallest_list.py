# Largest and Smallest in a List

total_elements = int(input("Enter number of elements: "))

my_list = []

for index in range(total_elements):
    number = int(input("Enter a number: "))
    my_list.append(number)

if total_elements > 0:
    print("Largest element:", max(my_list))
    print("Smallest element:", min(my_list))
else:
    print("List is empty")