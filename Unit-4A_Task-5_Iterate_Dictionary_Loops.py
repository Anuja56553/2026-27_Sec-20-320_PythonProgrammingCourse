subjects = {}

for i in range(3):
    subject = input("Enter subject: ")
    marks = int(input("Enter marks: "))
    subjects[subject] = marks

print("Keys:")
for key in subjects.keys():
    print(key)

print("Values:")
for value in subjects.values():
    print(value)

print("Items:")
for key, value in subjects.items():
    print(key, value)
