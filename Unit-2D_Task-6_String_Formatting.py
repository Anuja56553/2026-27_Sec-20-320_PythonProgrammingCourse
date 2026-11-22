# String Formatting

student_name = input("Enter student name: ")
student_age = int(input("Enter age: "))

# Using format()
print("My name is {} and my age is {}".format(student_name, student_age))

# Using f-string
print(f"My name is {student_name} and my age is {student_age}")

# Using % operator
print("My name is %s and my age is %d" % (student_name, student_age))