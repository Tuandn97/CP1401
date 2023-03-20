"""
CP1401 2022-3 Assignment 1
Program 3 – Sleep tracker
Name: Dao Ngoc Tuan
Date started: December 6th, 2022

Pseudocode:
NUMBER_OF_DAYS = 5
RECOMMENDED_SLEEP_HOURS_A_DAY = 8

total_sleep_hours = 0
total_recommended_sleep_hours = NUMBER_OF_DAYS * RECOMMENDED_SLEEP_HOURS_A_DAY
for i in range 1 to NUMBER_OF_DAYS + 1
    get sleep_hours
    while sleep_hours < 0 or sleep_hours > 24
        display Invalid number of hours
        get sleep_hours
    total_sleep_hours = total_sleep_hours + sleep_hours

( I use the for loop to ask the user to enter sleep_hours
because I know exactly how long the loop will loop (= NUMBER_OF_DAYS))
(I use the while loop to check the number of sleep_hours the user entered
because I don't know exactly how many times the user needs to enter correctly))

sleep_debt = total_recommended_sleep_hours - total_sleep_hours

display total_recommended_sleep_hours,total_sleep_hours
if total_sleep_hours >= total_recommended_sleep_hours
    display You are getting enough sleep. Keep it up!
else display sleep_debt
"""
NUMBER_OF_DAYS = 5
RECOMMENDED_SLEEP_HOURS_A_DAY = 8
MAXIMUM_HOURS = 24
MINIMUM_HOURS = 0
STARTED_DAY = 1
ONE = 1

total_sleep_hours = 0
total_recommended_sleep_hours = NUMBER_OF_DAYS * RECOMMENDED_SLEEP_HOURS_A_DAY
for i in range(STARTED_DAY, NUMBER_OF_DAYS + ONE):  # + ONE: to display and add the last number
    sleep_hours = float(input(f"Night {i} hours sleep: "))
    while sleep_hours < MINIMUM_HOURS or sleep_hours > MAXIMUM_HOURS:
        print("Invalid number of hours")
        sleep_hours = float(input(f"Night {i} hours sleep: "))
    total_sleep_hours += sleep_hours

sleep_debt = total_recommended_sleep_hours - total_sleep_hours

print(f"Recommended total sleep is: {total_recommended_sleep_hours:,.0f} "
      f"\nYour total hours of sleep : {total_sleep_hours:,.2f}")

if total_sleep_hours >= total_recommended_sleep_hours:
    print("You are getting enough sleep. Keep it up!")
else:
    print(f"Your sleep debt over this time is: {sleep_debt:,.2f}")
