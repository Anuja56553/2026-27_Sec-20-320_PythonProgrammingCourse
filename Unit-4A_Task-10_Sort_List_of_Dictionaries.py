students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students.append({"name": name, "marks": marks})

ascending = sorted(students, key=lambda x: x["marks"])
descending = sorted(students, key=lambda x: x["marks"], reverse=True)

print("Ascending Order:", ascending)
print("Descending Order:", descending)
