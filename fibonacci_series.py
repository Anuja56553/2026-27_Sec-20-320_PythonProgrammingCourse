total_terms = int(input("Enter number of terms: "))

first_term = 0
second_term = 1

for count in range(total_terms):
    print(first_term, end=" ")

    next_term = first_term + second_term
    first_term = second_term
    second_term = next_term