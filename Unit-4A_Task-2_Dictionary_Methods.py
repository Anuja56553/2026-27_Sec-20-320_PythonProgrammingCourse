name = input("Enter name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

student = {"name": name, "age": age, "course": course}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Name:", student.get("name"))

student.update({"age": int(input("Enter new age: "))})
print("Updated:", student)

student.pop("course")
print("After Pop:", student)
