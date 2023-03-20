# 1. Error Checking
"""
Algorithm
get worker_level
while worker_level < 0 or worker_level > 0
    display Invalid worker level
    get worker_level
salary = worker_level * 5000
display salary

"""
BASE_SALARY = 5000
MINIMUM_SALARY_LEVEL = 1
MAXIMUM_SALARY_LEVEL = 10

worker_level = int(input("Worker level:"))
while worker_level < MINIMUM_SALARY_LEVEL or worker_level > MAXIMUM_SALARY_LEVEL:
    print("Invalid worker level")
    worker_level = int(input("Worker level:"))

salary = BASE_SALARY * worker_level

print(f"With worker level {worker_level}, your salary is ${salary:,.2f}")
# 2. Number Sequences: a, b, c
# a:
for i in range(1, 100, 2):
    print(i)
print()
# b
for i in range(1896, 2023, 4):
    print(i, end=" ")
print()
# c: I will write a loop that displays all the SEA Games  years (every 2 years) since i was born (1997) until now
for i in range(1997, 2023, 2):
    print(i, end=" ")
print()

# 3. Menu :
"""
Algorithm
get user_choice (s, f, q)
while user_choice not q
    if user_choice is "s"
        display ":)"
    elif user_choice is "f"
        display ":("
    else display "Invalid choice"
    get user_choice (s, f, q)
display "Farewell"
    
"""
print("(S)miley", "(F)rowny", "(Q)uit", sep='\n')
user_choose = str(input().lower())

while user_choose != "q":
    if user_choose == "s":
        print(":)")
    elif user_choose == "f":
        print(":(")
    else:
        print("Invalid choice")
    print()
    print("(S)miley", "(F)rowny", "(Q)uit", sep='\n')
    user_choose = str(input().lower())

print("Farewell")

# 4. Accumulation:
# a. Average Age
"""
Algorithm 

total_age = 0
number_of_people = 0
get age
while  age <= 0 or age > 120
    total_age = total_age + age
    number_of_people = number_of_people + 1
    average_age = total_age / number_of_people 
    get age 
display average_age
"""
HIGHEST_AGE = 120
LOWEST_AGE = 0
ONE_PERSON = 1

total_age = 0
number_of_people = 0
average_age = 0

age = int(input(f"Enter the age value ({LOWEST_AGE} - {HIGHEST_AGE}) :"))

while LOWEST_AGE < age < HIGHEST_AGE:
    total_age += age
    number_of_people += ONE_PERSON
    average_age = total_age / number_of_people
    age = int(input(f"Enter the age value ({LOWEST_AGE} - {HIGHEST_AGE}) :"))
print("Invalid age")
print("Average age:", average_age, sep="", )

# b. Smileys Count
"""
Algorithm
number_of_smiley = 0
number_of_frowny = 0
COUNT_TIME = 1
get user_choice (s, f, q)
while user_choice not q
    if user_choice is "s"
        display ":)"
        number_of_smiley = number_of_smiley + COUNT_TIME
    elif user_choice is "f"
        display ":("
        number_of_frowny = number_of_frowny + COUNT_TIME
    else display "Invalid choice"
    get user_choice (s, f, q)
display "Farewell",  number_of_smiley, and number_of_frowny
"""
print("(S)miley", "(F)rowny", "(Q)uit", sep='\n')
user_choose = str(input().lower())

number_of_smiley = 0
number_of_frowny = 0

COUNT_TIME = 1

while user_choose != "q":
    if user_choose == "s":
        print(":)")
        number_of_smiley += COUNT_TIME
    elif user_choose == "f":
        print(":(")
        number_of_frowny += COUNT_TIME
    else:
        print("Invalid choice")
    print()
    print("(S)miley", "(F)rowny", "(Q)uit", sep='\n')
    user_choose = str(input().lower())

print(f"Farewell, You choose {number_of_smiley} smiley face and {number_of_frowny} frowny face ")

# c.Total Numbers
"""
Algorithm

get number_of_repetition
repeat i in range from 1 to (number_of_repetition +1)
    get number(i) 
    total = total + number
display number_of_repetition, total
"""
total = 0
number_of_repetition = int(input(f"How many numbers do you want to add up? "))
for i in range(1, number_of_repetition + 1):
    number = float(input(f"Enter number {i}: "))
    total += number
print(f"The total of those {number_of_repetition} numbers is {total:,.0f}")

# Guessing Game
"""
Algorithm

SECRET_NUMBER = 6
get user_guess
guess_time = 0

while user_guess not SECRET_NUMBER
    if user_guess < SECRET_NUMBER
    display Higher
    else display Lower
    guess_time = guess_time + 1
    get user_guess
Print You got it in "guess_time"  guesses!
"""
SECRET_NUMBER = 6
ONE_TIME = 1
guess_time = 0

user_guess = float(input(f"Guess a number: "))
while user_guess != SECRET_NUMBER:
    if user_guess < SECRET_NUMBER:
        print("Higher")
    else:
        print("Lower")
    user_guess = float(input(f"Guess a number: "))
    guess_time += ONE_TIME
guess_time += ONE_TIME

print(f"You got it in {guess_time} guesses!")

# Nested Loops
"""
get Rows
get Columns

for row_counter in range 0 - Rows
    for columns_counter in range 0 - Columns
        display columns_counter
    display ()

"""
rows = int(input("Rows: "))
columns = int(input("Columns: "))
for row_counter in range(rows):
    for columns_counter in range(columns):
        print(columns_counter, end=" ")
    print()
