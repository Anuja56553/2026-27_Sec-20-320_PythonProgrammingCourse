def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

name = input("Enter student name: ")
python = int(input("Enter Python marks: "))
java = int(input("Enter Java marks: "))
html = int(input("Enter HTML marks: "))

student_details(name=name, Python=python, Java=java, HTML=html)
