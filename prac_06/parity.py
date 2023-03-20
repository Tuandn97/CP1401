# PARITY
"""
function main()
    get number
    display_parity(number)
    parity = calculate_parity(number)
    display is_odd(parity)


function display_parity(number) #PART 1
    display the parity


function calculate_parity(number) #PART 2
    result = number % 2
    return result


function is_odd(parity)
    if parity == 1
        return "odd"
    else:
        return "even"
"""


def main():
    number = int(input("Number: "))
    display_parity(number)
    parity = calculate_parity(number)
    print(f"{number} is an {is_odd(parity)} number")


def display_parity(number):
    print(f"parity of {number} should be {number % 2}: {number % 2}")


def calculate_parity(number):
    result = number % 2
    return result


def is_odd(parity):
    if parity == 1:
        return "odd"
    else:
        return "even"


main()
