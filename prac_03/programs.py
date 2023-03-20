#A1. Tax
"""
Algorithm
get income
if income < 100
    total_tax = 0
 else if income <= 500
    total_tax = income * 0.02
else if income <= 1000
    total_tax = income * 0.05
else
    total_tax = income * 0.1
money_take_home = income - total_tax
display total_tax, income
"""
TAX_RATE_LOW = 0.05
TAX_RATE_MID = 0.02
TAX_RATE_HIGH = 0.1
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_MID = 500
TAX_THRESHOLD_HIGH = 1000
NO_TAX = 0

print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $"))
if income < TAX_THRESHOLD_LOW:
    total_tax = NO_TAX
elif income <= TAX_THRESHOLD_MID:
    total_tax = TAX_RATE_LOW * income
elif income <= TAX_THRESHOLD_HIGH:
    total_tax = TAX_RATE_MID * income

else:
    total_tax = TAX_RATE_HIGH * income

take_home_pay = income - total_tax

print("Total tax is: $", total_tax, sep="")
print("Take home pay is: $", take_home_pay, sep="")


#B. Car Insurance
"""
Algorithm
get the applicant_age
if applicant_age < 18
    display Hire refused
if else applicant's_age < 25
    display Insurance required
else 
    display Insurance not required
display insurance_status
"""
applicant_age = int(input("Please enter your age here: "))

if applicant_age < 18:
    print("Hire refused")
elif applicant_age < 25:
    print("Insurance required")
else:
    print("Insurance not required")

#C. Simple Password Checker
"""
Algorithm
get user_password
SECRET_PASSWORD = 123qwe
if user_password == SECRET_PASSWORD
    display Access granted
else display Access denied

"""
SECRET_PASSWORD = "123qwe"

user_password = str(input("Password: "))

if user_password == SECRET_PASSWORD:
    print("Access granted")
else:
    print("Access denied")
#D. Dog Years
"""
Algorithm
get  age_in_human_years
if  age_in_human_years  <= 2
    age_in_dog_years = age_in_human_years * 10.5
else
    age_in_dog_years = 21 + (age_in_human_years - 2) * 4
display age_in_dog_years

"""
FIRST_AGE_RATE_PERIOD = 10.5
SECOND_AGE_RATE_PERIOD = 4
FIRST_PERIOD = 2

age_in_human_years = int(input("Age in human years:"))

if age_in_human_years <= FIRST_PERIOD:
    age_in_dog_years = age_in_human_years * FIRST_AGE_RATE_PERIOD
else:
    age_in_dog_years = (FIRST_AGE_RATE_PERIOD * FIRST_PERIOD) + (age_in_human_years-FIRST_PERIOD) * SECOND_AGE_RATE_PERIOD

print("Age in dog years is ", age_in_dog_years, sep="")

#E. Rock of Ages
"""
Algorithm
get user_age
if user_age <0 or user_age >120
    display Invalid age
else if user_age <= 20 
    display You are so Young
else if user_age <= 60
    display You are still young 
else if user_age <= 100
    display Have a good day
else 
    display You look so strong in this age
"""
YOUNG_AGE = 20
MID_AGE = 60
OLD_AGE = 100
LOWEST_AGE = 0
HIGHEST_AGE = 120

user_age = int(input("Enter your age:"))

if user_age < LOWEST_AGE or user_age > HIGHEST_AGE:
    print("Invalid age")
elif user_age <= YOUNG_AGE:
    print("You are so Young")
elif user_age <= MID_AGE:
    print("You are still young")
elif user_age <= OLD_AGE:
    print("Have a good day")
else:
    print("You look so strong in this age")

#F. Speeding Fines
"""
Algorithm
get user_speed, speed_limit (in km)
speed_over_the_limit = user_speed - seed_limit

if speed_over_the_limit < 13 
    penalty_amount = 177
if else speed_over_the_limit <= 20
    penalty_amount = 266
if else speed_over_the_limit <= 30 
    penalty_amount = 444
if else speed_over_the_limit <= 40
    penalty_amount = 622
else  penalty_amount = 1245

"""
INFRINGEMENT_LEVEL_1 = 13
INFRINGEMENT_LEVEL_2 = 20
INFRINGEMENT_LEVEL_3 = 30
INFRINGEMENT_LEVEL_4 = 40

user_speed = float(input("Enter your speed: "))
speed_limit = float(input("Enter the speed limit:"))

speed_over_the_limit = user_speed - speed_limit

if speed_over_the_limit < INFRINGEMENT_LEVEL_1:
    penalty_amount = 177
elif speed_over_the_limit <= INFRINGEMENT_LEVEL_2:
    penalty_amount = 266
elif speed_over_the_limit <= INFRINGEMENT_LEVEL_3:
    penalty_amount = 622
elif speed_over_the_limit <= INFRINGEMENT_LEVEL_4:
    penalty_amount = 1245
else:
    penalty_amount = 1245

print("Your Penalty amount is ", penalty_amount, sep="" )


