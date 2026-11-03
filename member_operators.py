# Membership Operators

numbers_list = [10, 20, 30, 40, 50]

search_number = int(input("Enter number to search: "))

present_result = search_number in numbers_list
absent_result = search_number not in numbers_list

print("Number is present =", present_result)
print("Number is absent =", absent_result)