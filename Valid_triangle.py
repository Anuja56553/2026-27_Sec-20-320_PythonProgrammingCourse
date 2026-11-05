# Valid Triangle Using Three Angles

first_angle = int(input("Enter first angle: "))
second_angle = int(input("Enter second angle: "))
third_angle = int(input("Enter third angle: "))

total_angle = first_angle + second_angle + third_angle

if first_angle > 0 and second_angle > 0 and third_angle > 0 and total_angle == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")