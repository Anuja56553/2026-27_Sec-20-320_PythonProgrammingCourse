dict1 = {}
dict2 = {}

n = int(input("Enter number of items in first dictionary: "))
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict1[key] = value

m = int(input("Enter number of items in second dictionary: "))
for i in range(m):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict2[key] = value

merged = dict1.copy()
merged.update(dict2)

print("First Dictionary:", dict1)
print("Second Dictionary:", dict2)
print("Merged Dictionary:", merged)
