first_list = [10, 20, 30]
second_list = first_list
third_list = [10, 20, 30]

result_one = first_list is second_list
result_two = first_list is third_list
result_three = first_list is not third_list

print("First is Second =", result_one)
print("First is Third =", result_two)
print("First is not Third =", result_three)
