# 7. BMI Files
"""
pseudocode
function question_7()
    open "bmis.txt" file for writing  as in_file
    get number_people
    for i in range number_people
        get weight, height
        bmi = calculate_bmi(height,weight)
        category = determine_weight_category(bmi)
        write bmi, category into bmis.txt
    close bmis.txt file
    open "bmis.txt" file for reading  as in_file
    for line in in_file:
        bmi, category = remove the and split the value by the "space"
    display bmi, category

function calculate_bmi(height,weight)
    return weight / (height ** 2)

function determine_weight_category(bmi)
    if bmi < 18.5
        return "underweight"
    elif bmi < 25
        return "normal"
    elif bmi < 30
        return "overweight"
    else
        return "obese"
"""
HEIGHT = 1.75
STARTS_WEIGHT = 50
ENDS_WEIGHT = 101
STEPS_WEIGHT = 2

UNDERWEIGHT = 18.5
NORMAL = 25
OVERWEIGHT = 30


def main():
    """ The main function of the program. Open file to write and read."""
    in_file = open("bmis.txt", 'w')
    number_people = int(input(f"Number of people: "))
    for i in range(number_people):
        weight = float(input(f"Weight: "))
        height = float(input(f"Height: "))
        bmi = calculate_bmi(height, weight)
        category = determine_weight_category(bmi)
        print(bmi, category, file=in_file)
    in_file.close()
    in_file = open("bmis.txt", 'r')
    for line in in_file:
        bmi, category = line.strip().split(" ")
        print(f"BMI {float(bmi):.1f}, considered  {category}")


def calculate_bmi(height, weight):
    """Calculate BMI based on height and weight"""
    return weight / (height ** 2)  # Number 2 here is from the formula


def determine_weight_category(bmi):
    """Determine category based on BMI"""
    if bmi < UNDERWEIGHT:
        return "underweight"
    elif bmi < NORMAL:
        return "normal"
    elif bmi < OVERWEIGHT:
        return "overweight"
    else:
        return "obese"


main()
