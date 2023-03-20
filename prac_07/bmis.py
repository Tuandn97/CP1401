# BMIs
"""
Pseudocode
function main
    for weight in range (50,101, 2)
        bmi = calculate_bmi(1.75,weight)
        category = determine_weight_category(bmi)
        display bmi, category

function calculate_bmi(1.75,weight)
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
    for weight in range(STARTS_WEIGHT, ENDS_WEIGHT, STEPS_WEIGHT):
        bmi = calculate_bmi(HEIGHT, weight)
        category = determine_weight_category(bmi)
        print(f"Height {HEIGHT}m, Weight{weight:4}kg = BMI {bmi:,.1f}, considered {category}")


def calculate_bmi(height, weight):
    return weight / (height ** 2)  # Number 2 here is from the formula


def determine_weight_category(bmi):
    if bmi < UNDERWEIGHT:
        return "underweight"
    elif bmi < NORMAL:
        return "normal"
    elif bmi < OVERWEIGHT:
        return "overweight"
    else:
        return "obese"


main()
