print("(I)nstructions", "(C)alculate", "(Q)uit", sep='\n')
user_reply = input().upper()

while user_reply != "I" and user_reply != "C" and user_reply != "Q":
    print("Invalid input")
    print("(I)nstructions", "(C)alculate", "(Q)uit", sep='\n')
    user_reply = input().upper()

while user_reply == "I" or user_reply == "C" or user_reply == "Q":
    if user_reply == "I":
        print("Enter the number of products you want to buy and your chosen price. If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!")
        print("(I)nstructions", "(C)alculate", "(Q)uit", sep='\n')
        user_reply = input().upper()

    elif user_reply == "C":
        number_of_products = int(input("Enter number of productis: "))
        while number_of_products < 0:
            print("Invalid number of products!")
            number_of_products = int(input("Enter number of products: "))
        price_of_products = float(input("Enter the price: "))
        while price_of_products < 0:
            print("Invalid Price")
            price_of_products = float(input("Enter the price: "))
        if number_of_products >5:
            total_cost = (number_of_products * price_of_products) - number_of_products * 0.1 * price_of_products
        else:
            total_cost = number_of_products * price_of_products
            print(total_cost)
            print("(I)nstructions", "(C)alculate", "(Q)uit", sep='\n')
            user_reply = input().upper()
if user_reply == "Q":
     print("Fare well")


