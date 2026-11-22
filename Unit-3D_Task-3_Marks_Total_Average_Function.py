# Total and Average Marks Using Function

def calculate_marks(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3
    return total, average

mark1 = float(input("Enter first subject marks: "))
mark2 = float(input("Enter second subject marks: "))
mark3 = float(input("Enter third subject marks: "))

total, average = calculate_marks(mark1, mark2, mark3)

print("Total marks:", total)
print("Average marks:", average)