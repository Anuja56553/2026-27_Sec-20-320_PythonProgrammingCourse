# Area and Perimeter of a Rectangle Using Function

def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area, perimeter = rectangle(length, breadth)

print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)