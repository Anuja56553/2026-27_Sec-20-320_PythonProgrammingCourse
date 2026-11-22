def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

print_details(name=name, age=age, city=city)