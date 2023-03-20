"""
CP1401 2022-1 Assignment 2
Market Garden Simulator
Student Name: Dao Ngoc Tuan
Date started: January 21, 2023

Pseudocode:
import the random function


function main()
    day = 0
    total_food = 0
    plants = empty list
    display welcome message
    get plants_source (yes/no)
    plants = determine_plants_source(plants_source, plants)
    for plant in plants
        display plants
    total_plant  =  the length of plants(list)

    display menu
    get choice
    while choice is difference "Q"
        if choice is "W"
            day, total_food, total_plant = simulate_day(day, plants, total_food, total_plant)
        else if choice is "D"
            display_plant(total_plant, plants)
        else if choice is "A"
            plants = add_plant(total_food, plants)
            total_plant  =  the length of plants(list)
        else
            display Error message
        display day, total_plant,total_food,menu
        get choice
        if total_plant is  0
       display You finished with no plants
    else
        display plants
        display_plant(total_plant, plants)
        display day, total_plant,total_food
    get save_or_not
    if save_or_not is difference "n"
        save_file(plants)
    display Thank you for simulating. Now enjoy some real plants

function simulate_a_day
    day = day + 1
    random_rainfall = random between 0 and 128 mm
    display random_rainfall
    if random_rainfall < 32
        total_plant = choose_dead_plant(plants, total_plant)
    else
        total_food = calculate_food_produced(plants, random_rainfall, total_food)
    return day, total_food, total_plant


function calculate_food_produced(plants, random_rainfall, total_food)
    for plant in plants
        percent = random value between 1/3 rainfall and actual rainfall / 128
        food_produced = percent * length of plant
        total_food = total_food + food_produced_
        display food_produced, total_food
    return total_food

function choose_dead_plant(plants, total_plant)
    if total_plant > 0
        dead_plant = random from the plants list
        remove the dead_plant out of the plants list
        total_plant  =  the length of plants(list)
        display dead_plant
    return total_plant

function determine_plants_source (plants_source, plants)
    if plants_source == y
        open "plants.txt" for reading as in_file
        for plant in in_file
            add plant to plants
        close in_file
    else plants = Parsley, Sage, Rosemary, Thyme
    return plants


function display_plant(total_plant, plants)
    if total_plant > 0
        for plant in plants
            if plant is the same as  plants[-1]
                display plant
            else
                display plant with "," in the end
    else
       display a line

function add_plant(total_food, plants)
    get new_plant
    plant_price = the length of new_plant
    if plant_price > total_food
        display plant_price total_food
    else
        add plant to plants
    return plants


function get_valid_name(prompt, plants)
    get name
    while name is empty string or name in plants
        if name is empty
            display Invalid plant name
        else
            display You already have this plant
        get name
    return name


function save_file(plants)
    open "plants.txt" for writing as in_file
    for plant in plants
        write plant to plants.txt file
    close in_file
    display Saved

"""
import random

WELCOME_MASSAGE = f"Welcome to my garden." \
    f"\nPlants cost and generate food according to their name length (e.g., Sage plants cost 4)." \
    f"\nYou can buy new plants with the food your garden generates." \
    f"\nYou get up to 128 mm of rain per day. Not all plants can survive with less than 32." \
    f"\nEnjoy :)"

STANDARD_PLANTS = ["Parsley", "Sage", "Rosemary", "Thyme"]
MIN_RAINFALL = 0
MAX_RAINFALL = 128
MIN_PLANTS = 0
THRESHOLD_RAINFALL = 32
MENU = f"\n(W)ait" \
       f"\n(D)isplay plants" \
       f"\n(A)dd new plant" \
       f"\n(Q)uit"


def main():
    """Program for Market Garden Simulator."""
    total_food = 0
    day = 0
    plants = []
    print(WELCOME_MASSAGE)
    plants_source = input(f"Would you like to load your plants from plants.txt (Y/n)?")
    plants = determine_plants_source(plants_source, plants)
    print(f"You start with these plants:")
    total_plant = len(plants)
    display_plant(total_plant, plants)
    print(f"After {day} days, you have {total_plant} plants and your total food is {total_food}."
          f"{MENU}")
    choice = input("Choose:").upper()
    while choice != "Q":
        if choice == "W":
            day, total_food, total_plant = simulate_a_day(day, plants, total_food, total_plant)
        elif choice == "D":
            display_plant(total_plant, plants)
        elif choice == "A":
            plants = add_plant(total_food, plants)
            total_plant = len(plants)
        else:
            print("Invalid choice")
        print(f"After {day} days, you have {total_plant} plants and your total food is {total_food}."
              f"{MENU}")
        choice = input("Choose:").upper()
    if total_plant == MIN_PLANTS:
        print("You finished with no plants.")
    else:
        print("You finished with these plants:", sep=" ")
        display_plant(total_plant, plants)
        print(f"After {day} day(s), you have {total_plant} plant(s) and your total food is {total_food}.", sep=" ")
    save_or_not = input("Would you like to save your plants to plants.txt?").lower()
    if save_or_not != "n":
        save_file(plants)
    print("Thank you for simulating. Now enjoy some real plants.")


def simulate_a_day(day, plants, total_food, total_plant):
    """Simulating a day when users want to wait"""
    day += 1  # add one day
    random_rainfall = random.randint(MIN_RAINFALL, MAX_RAINFALL)
    print(f"Rainfall: {random_rainfall}mm")
    if random_rainfall < THRESHOLD_RAINFALL:
        total_plant = choose_dead_plant(plants, total_plant)
    else:
        total_food = calculate_food_produced(plants, random_rainfall, total_food)
        print("")  # Newline
    return day, total_food, total_plant


def choose_dead_plant(plants, total_plant):
    """Choosing a dead plant from the plants list when rainfall below 32"""
    if total_plant > MIN_PLANTS:
        dead_plant = random.choice(plants)
        plants.remove(dead_plant)
        total_plant = len(plants)
        print(f"Sadly, your {dead_plant} plant has died.")
    return total_plant


def calculate_food_produced(plants, random_rainfall, total_food):
    """calculate the food produced of each plant after a day"""
    for plant in plants:
        percent = random.randint(int((1 / 3) * random_rainfall), random_rainfall) / MAX_RAINFALL
        # the number 1/3 is taken from the formula
        food_produced = percent * len(plant)
        total_food += int(food_produced)
        if plant == plants[-1]:  # Check if the plant is the last element
            print(f"{plant} produced {int(food_produced)}")  # display plant without "," in the end
        else:
            print(f"{plant} produced {int(food_produced)}", end=", ")

    return total_food


def determine_plants_source(plants_source, plants):
    """Choosing the source the load the list of plant"""
    if plants_source == "n":
        plants = STANDARD_PLANTS
    else:
        in_file = open("plants.txt", 'r')
        for plant in in_file:
            plants.append(plant)
        in_file.close()

    return plants


def display_plant(total_plant, plants):
    """Displays the current plants"""
    if total_plant > MIN_PLANTS:
        for plant in plants:
            if plant == plants[-1]:  # Check if the plant is the last element
                print(plant.title())  # display plant without "," in the end
            else:
                print(plant.strip().title(), end=", ")
    else:
        print("")  # print nothing


def add_plant(total_food, plants):
    """check if user has enough food to afford it and Adds plant to list of current plants."""
    new_plant = get_valid_name("Enter plant name: ", plants)
    plant_price = len(new_plant)
    if plant_price > total_food:
        print(f"{new_plant} would cost {plant_price} food. With only {total_food}, you can't afford it.")
    else:
        plants.append(new_plant)
    return plants


def get_valid_name(prompt, plants):
    """Get the valid name for the new_plant that user want to add"""
    name = input(prompt).title()
    while name == "" or name in plants:
        if name == "":
            print("Invalid plant name.")
        else:
            print(f"You already have a {name} plant.")
        name = input(prompt).title()

    return name


def save_file(plants):
    """Save the list of current plant to plants.txt file"""
    in_file = open("plants.txt", 'w')
    for plant in plants:
        print(plant, file=in_file, sep="")
    in_file.close()
    print("Saved")


main()
