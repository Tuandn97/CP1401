# Jerry the Driver

"""
Pseudocode

function main
    bank_balance = get_valid_number("Enter your Bank balance : $")
    speed_in_mph = get_valid_number("speed in mph")
    speed_limit_in_kph = get_valid_number("speed limit in kph")
    speed_in_kph = convert_miles_to_km(speed_in_mph)
    speed_over_the_limit = calculate_speed_over_limit(speed_in_kph, speed_limit_in_kph)
    fine = determine_fine(speed_over_the_limit)
    display fine

function get_valid_number(prompt, 0)
    get number
    while number < 0
        display Error message
        get number
    return number

function convert_miles_to_km (speed_in_mph)
    speed_in_kph = speed_in_mph * 1.60934
    return speed_in_kph

function  calculate_speed_over_limit(speed_in_km, speed_limit_in_kph)
    speed_over_the_limit = speed_in_kph - speed_limit_in_kph
    return speed_over_the_limit

function determine_fine (speed_over_the_limit)
    if speed_over_the_limit < 13
        fine = 177
    if else speed_over_the_limit <= 20
        fine = 266
    if else speed_over_the_limit <= 30
        fine = 444
    if else speed_over_the_limit <= 40
        fine = 622
    else  fine = 1245
    return fine

function calculate_speed_over_limit(speed_in_km,speed_limit_in_kph):
    speed_over_the_limit = speed_in_km - speed_limit_in_kph
    return speed_over_the_limit



"""
INFRINGEMENT_LEVEL_1 = 13
INFRINGEMENT_LEVEL_2 = 20
INFRINGEMENT_LEVEL_3 = 30
INFRINGEMENT_LEVEL_4 = 40

INVALID_NUMBER = 0
MILES_KM_RATIO = 1.60934


def main():
    """Display the text to get user input, calculate and print the fine to users"""
    speed_in_mph = get_valid_number("Speed in mph: ", INVALID_NUMBER)
    speed_limit_in_kph = get_valid_number("Speed limit in kph: ", INVALID_NUMBER)
    speed_in_kph = convert_miles_to_km(speed_in_mph)
    speed_over_the_limit = calculate_speed_over_limit(speed_in_kph, speed_limit_in_kph)
    fine = determine_fine(speed_over_the_limit)
    print(f"Your fine is: ${fine}, you had one job")


def get_valid_number(prompt, low):
    """Get the valid number and display Error message"""
    number = float(input(prompt))
    while number < low:
        print("Invalid input")
        number = float(input(prompt))
    return number


def convert_miles_to_km(speed_in_mph):
    """Convert from mph to kph"""
    speed_in_kph = speed_in_mph * MILES_KM_RATIO
    return speed_in_kph


def determine_fine(speed_over_the_limit):
    """ and determine the fine base on speed_over_the_limit """
    if speed_over_the_limit < INFRINGEMENT_LEVEL_1:
        return 177
    elif speed_over_the_limit <= INFRINGEMENT_LEVEL_2:
        return 266
    elif speed_over_the_limit <= INFRINGEMENT_LEVEL_3:
        return 444
    elif speed_over_the_limit <= INFRINGEMENT_LEVEL_4:
        return 622
    else:
        return 1245


def calculate_speed_over_limit(speed_in_kph, speed_limit_in_kph):
    """Calculate the speed over the limit base on speed_in_kph and speed_limit_in_kph """
    speed_over_the_limit = speed_in_kph - speed_limit_in_kph
    return speed_over_the_limit


def run_test():
    """Test the determine_fine function """
    fine = determine_fine(12)
    print(fine)  # It must be 177
    fine = determine_fine(19)
    print(fine)  # It must be 266
    fine = determine_fine(29)
    print(fine)  # It must be 444
    fine = determine_fine(39)
    print(fine)  # It must be 622
    fine = determine_fine(41)
    print(fine)  # It must be 1245


# run_test()
main()
