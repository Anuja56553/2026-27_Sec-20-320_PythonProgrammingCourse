# Character Frequency

text = input("Enter a string: ")

for character in text:
    if text.index(character) == text.index(character):
        if character not in text[:text.index(character)]:
            print(character, "=", text.count(character))