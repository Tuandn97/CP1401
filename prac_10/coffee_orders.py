"""
Pseudocode
MAIN_MENU = (O)rder - (D)rink - (R)andom choice - (Q)uit
coffee_menu = Flat White - Espresso - Long Black - Babyccino

function main()
    display Welcome to the IT@JCU Coffee Shop
    coffee_type = empty string
    display MAIN_MENU
    get user_choice
    while user_choice is not "Q"
        if user_choice is "O"
            coffee_type = get_coffee_type()
            print_introduction (coffee_type)
        else if user_choice is  "D"
            message = drink_coffee(coffee_type)
            display message
        else if user_choice is  "R"
            coffee_type = random_coffee_type()
            print_introduction(coffee_type)
        else
            display Invalid option
        display MAIN_MENU
        get user_choice
    display Thanks for drinking coffee



function get_coffee_type(coffee_menu)
    display Please choose from
    repeat coffee in COFFEE_MENU:
        display coffee and end with " - "
    get coffee_type ( title format)
    while coffee_type not in coffee_menu
        display Invalid order
        get coffee_type ( title format)
    return coffee_type

function print_introduction(coffee_type)
    display coffee_type
    if coffee_type is flat white
        grind_beans()
        pour_espresso()
        steam_milk()
        add_milk()
    else if coffee_type is "espresso"
        grind_beans()
        pour_espresso()
    else if  coffee_type is "long black"
        grind_beans()
        pour_espresso()
        print("- Add hot water to cup")
    else if coffee_type is Babyccino
        steam_milk()
        add_milk()
    else
        display Something went wrong! Unknown coffee

function grind_beans()
    Display instruction for grinding beans


function pour_espresso()
    Display instruction for pouring espresso


function steam_milk()
    Display instruction for steaming milk


function add_milk()
    Display instruction for adding milk


function drink_coffee(coffee_type)
    if coffee_type is empty
        return Oh... where's my coffee?
    else return Mmmm, nice coffee_type

function random_coffee_type(coffee_menu)
     return random in  coffee_menu list

"""
import random

MAIN_MENU = "(O)rder - (D)rink - (R)andom choice - (Q)uit"
COFFEE_MENU = ["Flat White", "Espresso", "Long Black", "Babyccino"]

def main():
    """Coffee ordering program"""
    coffee_type = ""
    print("Welcome to the IT@JCU Coffee Shop")
    user_choice = input(f"{MAIN_MENU}\n>>>").upper()
    while user_choice != "Q":
        if user_choice == "O":
            coffee_type = get_coffee_type()
            print_introduction(coffee_type)
        elif user_choice == "D":
            message = drink_coffee(coffee_type)
            print(message)
        elif user_choice == "R":
            coffee_type = random_coffee_type()
            print_introduction(coffee_type)
        else:
            print("Invalid option")
        user_choice = input(f"{MAIN_MENU}\n>>>").upper()
    print("Thanks for drinking coffee")


def get_coffee_type():
    """Get valid coffee order"""
    print("Please choose from: ")
    for coffee in COFFEE_MENU:
        print(coffee, end=" - ")
    coffee_type = input("? ").title()
    while coffee_type not in COFFEE_MENU:
        print("Invalid order")
        coffee_type = input("? ").title()
    return coffee_type


def print_introduction(coffee_type):
    """"Print instructions for the coffee_type"""
    print(f"Here's how to make a/n {coffee_type}")
    if coffee_type == "Flat White":
        grind_beans()
        pour_espresso()
        steam_milk()
        add_milk()
    elif coffee_type == "Espresso":
        grind_beans()
        pour_espresso()
    elif coffee_type == "Long Black":
        grind_beans()
        pour_espresso()
        print("- Add hot water to cup")
    elif coffee_type == "Babyccino":
        steam_milk()
        add_milk()
    else:   # Unexpected case
        print("Something went wrong! Unknown coffee.")


def grind_beans():
    """Print instruction for grinding beans """
    print("- Insert portafilter into grinder")
    print("- Press grind button to grind beans into portafilter")


def pour_espresso():
    """Print instruction for pouring espresso """
    print(f"-Distribute grounds"
          f"\n- Tamp grounds"
          f"\n- Insert full portafilter into group head"
          f"\n- Press shot button to pour espresso into cup")


def steam_milk():
    """Print instruction for steaming milk """
    print(f"- Fill jug with milk"
          f"\n- Steam milk until nice microfoam formed and milk up to temperature")


def add_milk():
    """Print instruction for adding milk """
    print(f"- Swirl milk gently in jug"
          f"\n- Pour milk into cup... carefully, artistically :)")


def drink_coffee(coffee_type):
    """determine the message for (D)rink """
    if coffee_type == "":
        return "Oh... where's my coffee?"
    else:
        return f"Mmmm, nice {coffee_type}"


def random_coffee_type():
    """Random the coffee_type from  coffee_menu """
    return random.choice(COFFEE_MENU)


main()

