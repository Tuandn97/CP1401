import random

# Constants
RAINFALL_MAX = 128
RAINFALL_MIN = 32
FOOD_PERCENT_MIN = 1 / 3
MENU = "\n(W)ait\n(D)isplay plants\n(A)dd new plant\n(Q)uit\n"

DEFAULT_PLANTS = ["Sage", "Thyme", "Rosemary", "Thai Basil"]


def main():
    day = 0
    food_total = 0
    plants = []
    print("Welcome to the my garden ")
    print("Plants cost and generate food according to their name length (e.g., Sage plants cost 4).")
    print("You can buy new plants with the food your garden generates.")
    print("You get up to 128 mm of rain per day. Not all plants can survive with less than 32..")
    print("Let's hope it rains... alot!")
    print("You start with these plants:")
    txt_choice = input("Would you like to load your plants from plants.txt (Y/n)").upper()
    if txt_choice == "N":
        plants = DEFAULT_PLANTS
    else:
        in_file = open("plants.txt", 'r')
        for plant in in_file:
            plants.append(plant)
        in_file.close()
    display_plants(plants)
    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input("Choose: ").upper()
        if choice == "W":
            food_total, day = simulate_day(food_total, day, plants)
        elif choice == "D":
            display_plants(plants)
        elif choice == "A":
            food_total = add_plant(food_total, plants)
        elif choice == "Q":
            print("Final details:")
            display_plants(plants)
            print(f"Number of days simulated: {simulate_day}")
            print(f"Number of plants: {len(plants)}")
            print(f"Total food produced: {food_total}")
            save_plants(plants)
            return
        else:
            print("Invalid choice.")
        print(f"After {day} days, you have {len(plants)} plants and your total food is {food_total}.")


def add_plant(food_total, plants):
    """Add a new plant to the garden, deducting its name length from food total"""
    plant_name = input("Enter the name of the new plant: ").title()
    # error check for blank input or existing plant
    while not plant_name or plant_name in plants:
        print("Invalid input. Plant name cannot be blank or already in the list.")
        plant_name = input("Enter the name of the new plant: ").title()
    food_total -= len(plant_name)
    plants.append(plant_name)
    print(f"{plant_name} has been added to the garden.")
    return food_total


def display_plants(plants):
    """Display the plants in the garden"""
    if len(plants) != 0: # check if there are any plants in the list
        print("Plants in the garden:")
        for plant in plants:
            print(plant)
    else:
        print("There are no plants in the garden.")


def simulate_day(food_total, day, plants):
    """Simulate a day with rainfall and calculate food produced by plants"""
    day += 1
    rainfall = random.randint(0, RAINFALL_MAX)
    if rainfall < RAINFALL_MIN:
        if plants:  # check if there are any plants in the list
            # randomly select a plant to die
            dead_plant = random.choice(plants)
            plants.remove(dead_plant)
            print(f"Unfortunately, the {dead_plant} has died due to lack of water.")
    else:
        result_str = ""
        percent = random.randint(int(FOOD_PERCENT_MIN * rainfall), rainfall) / RAINFALL_MAX
        for plant in plants:
            food_produced = int(percent * len(plant))
            food_total += food_produced
            result_str += f"{plant} produced {food_produced}, "
        print(result_str[:-2])  # Remove the last ", " from the string

    print(f"Rainfall: {rainfall}mm")
    return food_total, day


def save_plants(plants):
    """Save the plants in the garden to a file"""
    filename = input("Enter a filename to save the plants to: ")
    file = open(filename, "w")
    for plant in plants:
        file.write(plant + "\n")
    file.close()
    print(f"Plants saved to {filename}.")


main()

"""
def load_plants():
    plants = []
    filename = input("Enter the name of the file to load plants from: ")
    file = open(filename, 'r')
    plants = file.read().splitlines()
    file.close()
    return plants
"""
