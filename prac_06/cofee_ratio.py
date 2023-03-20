# 1. Coffee Brew Ratio

"""
Algorithm 1:
get dose, yield
ratio = yield / dose
if ratio < 2
        display ristretto
    if else ratio < 3
        display normale
    else
        display lungo

Algorithm 2:
function main
    get dose,yield
    ratio = calculate_ratio(dose, yield)
    coffee_style = determine_coffee_style
    display ratio and coffee_style

function calculate_ratio(dose, yield)
    ratio = yield / dose
    return

function determine_coffee_style(ratio) 
    if ratio < 2
        return ristretto
    else if ratio < 3
        return normale
    else
        return lungo

"""
RISTRETTO_RATIO = 2
NORMALE_RATIO = 3
LUNGO_RATI0 = 4


def main():
    dose = get_valid_number("Dose: ", 0, 100)
    yield_1 = get_valid_number("Yield: ", 0, 100)
    ratio = calculate_ratio(dose, yield_1)
    style = determine_coffee_style(ratio)
    print(f"1:{ratio:,.1f} is considered {style}")


def calculate_ratio(dose, yield_1):
    return yield_1 / dose


def determine_coffee_style(ratio):
    if ratio < RISTRETTO_RATIO:
        return "ristretto"
    elif ratio < NORMALE_RATIO:
        return "normale"
    else:
        return "lungo"


def check_coffee():
    ratio = determine_coffee_style(1)
    print(ratio)  # This should be ristretto
    ratio = determine_coffee_style(2)
    print(ratio)  # This should be normale
    ratio = determine_coffee_style(13.5)
    print(ratio)  # This should be lungo


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


main()
# check_coffee()
