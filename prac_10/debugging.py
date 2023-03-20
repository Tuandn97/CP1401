"""CP1401 - Practical 10 - Debugging.
Explain the problems (not the solution, not the style issues):
line 83: return result
Problem: This code means that it only returns the result in the else case,
if the result of "choice" and " "risk_chance" falls in the case of if and if else, the return value will be "non-type"

line  68: choice = 'x'
Problem: Wrong logic: We do not need to set choice = 'x' to start the loop below.
Just need to get user input first and check the condition in the while loop

Line 69-72 :
while choice not in VALID_CHOICES:
        choice = input("(C)onservative, (A)ggressive: ").upper()
        if choice not in VALID_CHOICES:
                print("Invalid choice"

Problem: Repeated code. The code will check this condition:  "choice not in VALID_CHOICES" two time.
One in while loop and one in if statement
...

Describe your debugging process:
1. Read line by line all the code to understand what the code about.
2. Note the line that I do not understand
3. Run and try all cases of this program:
- Test get_valid_amount function ( < 0 and > amount)
- Test the play function
    + Test Choice = C,  Choice = A, and Choice = anything
    + Add risk_chance = float(input("Risk chance: ")) and # risk_chance = random.randint(0, 101) to test the risk_chance
    (risk_chance = 40, risk_chance = 10, risk_chance = anything)
    + Print result to the what is return to main function
- Fix the error
...

Fix the code in-place below
"""
# Given code: This the code of the question
import random

VALID_CHOICES = 'AC'
CONSERVATIVE_CHANCE = 40
CONSERVATIVE_REWARD = 50
AGGRESSIVE_CHANCE = 10
AGGRESSIVE_REWARD = 80


def main():
    money = 100
    print("Welcome to the futility of gambling!")
    print("You start with a balance of $100.")
    while money > 0:
        result = play(money)
        money = money + result
        print(f"Your new balance is ${money}")
    print("You lost :)")


def get_valid_amount(balance, amount):
    while amount < 0 or amount > balance:
        print("Invalid amount")
        amount = int(input("Enter amount to play: "))
    return amount


def play(balance):
    """Calculate and display whether win or lose based on chance."""
    amount = int(input("Enter amount to play: "))
    amount_to_risk = get_valid_amount(balance, amount)
    choice = 'x'
    while choice not in VALID_CHOICES:
        choice = input("(C)onservative, (A)ggressive: ").upper()
        if choice not in VALID_CHOICES:
                print("Invalid choice")
    risk_chance = random.randint(0, 101)
    if choice == "C" and risk_chance <= CONSERVATIVE_CHANCE:
        result = (amount_to_risk * (CONSERVATIVE_REWARD / 100))
        print(f"Congratulations! You earned ${result:.2f}")
    elif choice == "A" and risk_chance <= AGGRESSIVE_CHANCE:
        result = (amount_to_risk * (AGGRESSIVE_REWARD / 100))
        print(f"Congratulations! You earned ${result:.2f}")
    else:
        result = -amount_to_risk
        print(f"You lost ${amount_to_risk:.2f}")
        return result


main()
# Fixed code: This tis the code after fixed

import random

VALID_CHOICES = 'AC'
CONSERVATIVE_CHANCE = 40
CONSERVATIVE_REWARD = 50
AGGRESSIVE_CHANCE = 10
AGGRESSIVE_REWARD = 80


def main_fixed():
    money = 100
    print("Welcome to the futility of gambling!")
    print("You start with a balance of $100.")
    while money > 0:
        result = play(money)
        money = money + result
        print(f"Your new balance is ${money}")
    print("You lost :)")


def get_valid_amount(prompt, balance):
    """change this function to use only one variable (amount_to_risk) """
    number = int(input(prompt))
    while number < 0 or number > balance:
        print("Invalid amount")
        number = int(input("Enter amount to play: "))
    return number


def play(balance):
    """Calculate and display whether win or lose based on chance."""
    amount_to_risk = get_valid_amount("Enter amount to play: ", balance)    # delete 1 variable amount and change all amount to amount_to_risk
    choice = input("(C)onservative, (A)ggressive: ").upper()    # Get choice first and then check
    while choice not in VALID_CHOICES:  # Delete the if statement and  check only condition in while loop
        print("Invalid choice")
        choice = input("(C)onservative, (A)ggressive: ").upper()
    risk_chance = random.randint(0, 101)
    # risk_chance = float(input("Risk chance: "))
    if choice == "C" and risk_chance <= CONSERVATIVE_CHANCE:
        result = (amount_to_risk * (CONSERVATIVE_REWARD / 100))
        print(f"Congratulations! You earned ${result:.2f}")
    elif choice == "A" and risk_chance <= AGGRESSIVE_CHANCE:
        result = (amount_to_risk * (AGGRESSIVE_REWARD / 100))
        print(f"Congratulations! You earned ${result:.2f}")
    else:
        result = -amount_to_risk
        print(f"You lost ${amount_to_risk:.2f}")
    # print(result)
    return result   # return should have the same level with if to return the result in all case


main_fixed()