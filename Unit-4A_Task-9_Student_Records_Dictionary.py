name = input("Enter student name: ")
marks = int(input("Enter marks: "))
grade = input("Enter grade: ")

student = {"name": name, "marks": marks, "grade": grade}

print("Student Name:", student["name"])
print("Marks:", student["marks"])
print("Grade:", student["grade"])
