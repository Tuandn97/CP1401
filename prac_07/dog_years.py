# Dog Years
"""
Pseudocode
function main
    get  human_years
    while human_years > 0
        dog_years = calculate_dog_years(human_years)
        display dog_years
        get  human_years

function calculate_dog_years(human_years)
    if  age_in_human_years  <= 2
        dog_years = human_years * 10.5
    else
        dog_years = 21 + (human_years - 2) * 4


"""
FIRST_AGE_RATE_PERIOD = 10.5
SECOND_AGE_RATE_PERIOD = 4
FIRST_PERIOD = 2
FIRST_PERIOD_DOG_YEAR = 21
MINIMUM_AGE = 0


def main():
    """Get user input, display the Dog years and loop until user enter the negative number"""
    human_years = int(input("Age in human years: "))
    while human_years > MINIMUM_AGE:
        dog_years = calculate_dog_years(human_years)
        print("Age in dog years is: ", dog_years, sep="")
        human_years = int(input("Age in human years: "))


def calculate_dog_years(human_years):
    """Calculate the dog year from human years"""
    if human_years <= FIRST_PERIOD:
        dog_years = human_years * FIRST_AGE_RATE_PERIOD
    else:
        dog_years = FIRST_PERIOD_DOG_YEAR + (human_years - FIRST_PERIOD) * SECOND_AGE_RATE_PERIOD
    return dog_years


main()
