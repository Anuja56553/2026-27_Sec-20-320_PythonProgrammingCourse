name1 = input("Enter first student name: ")
marks1 = int(input("Enter first student marks: "))

name2 = input("Enter second student name: ")
marks2 = int(input("Enter second student marks: "))

students = {
    "student1": {"name": name1, "marks": marks1},
    "student2": {"name": name2, "marks": marks2}
}

for student in students.values():
    print("Name:", student["name"])
    print("Marks:", student["marks"])
