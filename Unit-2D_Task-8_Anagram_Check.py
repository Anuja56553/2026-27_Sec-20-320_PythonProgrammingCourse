# Anagram Check

first_string = input("Enter first string: ")
second_string = input("Enter second string: ")

first_string = first_string.replace(" ", "").lower()
second_string = second_string.replace(" ", "").lower()

if sorted(first_string) == sorted(second_string):
    print("Anagrams")
else:
    print("Not Anagrams")