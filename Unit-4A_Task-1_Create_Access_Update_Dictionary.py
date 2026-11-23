name = input("Enter name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

student = {"name": name, "age": age, "course": course}

print("Student Dictionary:", student)

student["age"] = int(input("Enter updated age: "))
student["city"] = input("Enter city: ")

print("Updated Dictionary:", student)
