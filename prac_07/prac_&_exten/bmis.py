# BMIs
"""
Pseudocode
function main
    for height in range ( 150,200, 10)
        height_m = height_cm / 100
        for weight in range (50,101, 2)
            bmi = calculate_bmi(height_cm,weight)
            category = determine_weight_category(bmi)
            display bmi, category

function calculate_bmi(height_cm,weight)
    return weight / (height_cm ** 2)

function determine_weight_category(bmi)
    if bmi < 18.5
        return "underweight"
    else if bmi < 25
        return "normal"
    else if bmi < 30
        return "overweight"
    else
        return "obese"
"""
STARTS_WEIGHT = 50
ENDS_WEIGHT = 101
STEPS_WEIGHT = 10

STARTS_HEIGHT = 150
ENDS_HEIGHT = 191
STEPS_HEIGHT = 10

UNDERWEIGHT = 18.5
NORMAL = 25
OVERWEIGHT = 30

M_CM_RATIO = 100


def main():
    """Loop height in cm and weight in m to have the same output that the question required  """
    for height_cm in range(STARTS_HEIGHT, ENDS_HEIGHT, STEPS_HEIGHT):
        height_m = height_cm / M_CM_RATIO   # Covert the height to meter to display
        for weight in range(STARTS_WEIGHT, ENDS_WEIGHT, STEPS_WEIGHT):
            bmi = calculate_bmi(height_m, weight)
            category = determine_weight_category(bmi)
            print(f"Height {height_m}m, Weight{weight:4}kg = BMI {bmi:,.1f}, considered {category}")


def calculate_bmi(height_m, weight):
    """Calculate the BMI base on Height and weight """
    return weight / (height_m ** 2)  # Number 2 here is from the formula


def determine_weight_category(bmi):
    """Determine the category base on the BMI that was calculated in calculate_bmi funciton """
    if bmi < UNDERWEIGHT:
        return "underweight"
    elif bmi < NORMAL:
        return "normal"
    elif bmi < OVERWEIGHT:
        return "overweight"
    else:
        return "obese"


main()
