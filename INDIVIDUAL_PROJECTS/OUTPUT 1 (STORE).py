#Working Cashier Input
#Calculator

fruit = ("apple", "banana", "mango")
apple = 10
banana = 15
mango = 20



item = input("Pick a fruit to buy: ")
if item == fruit[0]:
    second = (input("Apple is $10, Would you like to purchase it? "))
    if second == "yes":
        cash = int(input("Enter amount: $"))
        total = cash - apple
        if total == 0:
            print("Thank you for your purchase!")
        else:
            print(f"Your change is ${total} Thank you for your purchase!")

if item == fruit[1]:
    second = (input("Banana is $15, Would you like to purchase it? "))
    if second == "yes":
        cash = int(input("Enter amount: $"))
        total = cash - banana
        if total == 0:
            print("Thank you for your purchase!")
        else:
            print(f"Your change is ${total} Thank you for your purchase!")

if item == fruit[2]:
    second = (input("Mango is $15, Would you like to purchase it? "))
    if second == "yes":
        cash = int(input("Enter amount: $"))
        total = cash - mango
        if total == 0:
            print("Thank you for your purchase!")
        else:
            print(f"Your change is ${total} Thank you for your purchase!")
