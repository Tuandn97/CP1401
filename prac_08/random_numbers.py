# Random numbers
"""
Pseudocode
import random
numbers = empty list
get random_numbers, maximum_number
repeat number in range (random_numbers)
    number = random an integer from 0 to  maximum_number
    add number to numbers
display numbers, max number from the numbers list , min number from the numbers list
random_index = random  an integer from 0 to  random_numbers - 1
display numbers[random_index]
revert numbers
display numbers
sort numbers
display numbers

"""
import random

MINIMUM_NUMBER = 0

numbers = []
random_numbers = int(input("How many random numbers: "))
maximum_number = int(input("Maximum number: "))
for number in range(random_numbers):
    number = random.randint(MINIMUM_NUMBER, maximum_number)
    numbers.append(number)
random_index = random.randint(MINIMUM_NUMBER, random_numbers - 1)   # Minus 1 because the index count from 0
chosen_number = numbers[random_index]
print(f"The numbers are: {numbers}"
      f"\nThe minimum is {min(numbers)}"
      f"\nThe maximum is {max(numbers)}"
      f"\nA randomly chosen number is {chosen_number}")
numbers.reverse()
print(f"The numbers reversed are {numbers}")
numbers.sort()
print(f"The numbers sorted are: {numbers}")
