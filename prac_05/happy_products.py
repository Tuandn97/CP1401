"""
menu = instructions calculate quit
display menu
get user_choice
while user_choice is not q
    if user_choice is i
        display "Enter the number of products you want to buy and your chosen price.
        If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!"
        display menu
        get user_choice
    else if user_choice is c
        get number_of_products
        while number_of_products < 0
            display Invalid input
            get number_of_products
        get price
        while price <= 0
            print Invalid input
            get price
        if number_of_products > 5
            total_cost = (number_of_products * price) - (number_of_products * price * 10%)
        else total_cost = number_of_products * price
        display total_cost
        display menu
        get user_choice
    else display  Invalid choice
        display menu
        get user_choice
display Farewell


"""
DISCOUNT = 0.1
MINIMUM_PRODUCT = 0
DISCOUNT_POINT = 5
MINIMUM_PRICE = 0
MENU = "Menu:\n(I)nstructions\n(C)alculate\n(Q)uit"

print(MENU)
user_choice = input("Choice: ").upper()
while user_choice != "Q":
    if user_choice == "I":
        print(f"Enter the number of products you want to buy and your chosen price.\nIf you buy 0-5 items, "
              f"they're full price, over 5 items and each one is 10% off!")
        print(MENU)
        user_choice = input("Choice: ").upper()
    elif user_choice == "C":
        number_of_products = int(input("Number of products: "))
        while number_of_products < MINIMUM_PRODUCT:
            print("Invalid input")
            number_of_products = int(input("Number of products: "))
        price = float(input("Price:"))
        while price <= MINIMUM_PRICE:
            print("Invalid input")
            price = float("Price: ")
        if number_of_products > DISCOUNT_POINT:
            total_cost = (number_of_products * price) - (number_of_products * price * DISCOUNT)
        else:
            total_cost = number_of_products * price
        print(f"{number_of_products} x ${price:,.2f} products = ${total_cost:,.2f}")
        print(MENU)
        user_choice = input("Choice: ").upper()
    else:
        print("Invalid choice")
        user_choice = input("Choice: ").upper()

print("Farewell")
