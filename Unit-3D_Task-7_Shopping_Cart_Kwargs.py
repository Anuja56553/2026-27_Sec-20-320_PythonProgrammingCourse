def shopping_cart(**products):
    total = 0

    for item, price in products.items():
        print(item, ": ₹", price)
        total = total + price

    print("Total Amount: ₹", total)

apple = int(input("Enter apple price: "))
orange = int(input("Enter orange price: "))
mango = int(input("Enter mango price: "))

shopping_cart(apple=apple, orange=orange, mango=mango)