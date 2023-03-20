"""
CP1401 2022-3 Assignment 1
Program 1 – Pay CalculatorStudent 
Name: Dao Ngoc Tuan
Date started: December 5th, 2022

Pseudocode:
BASE_PAY = 45.00
get worked_hours, experience_level
total_bonus_percentage =  experience_level * 5%
pay_rate = (total_bonus_percentage * BASE_PAY) + BASE_PAY
total_pay = pay_rate * worked_hours
display total_pay, pay_rate
"""
BONUS_PERCENTAGE = 0.05
BASE_PAY = 45.00

print("Experience Counts Pay Calculator")
worked_hours = float(input("Number of hours worked: "))
experience_level = int(input(f"\t  Experience level: "))

total_bonus_percentage = experience_level * BONUS_PERCENTAGE
pay_rate = (total_bonus_percentage * BASE_PAY) + BASE_PAY
total_pay = pay_rate * worked_hours

print(f"Based on your experience level ({experience_level}):\nYour hourly pay rate is ${pay_rate:.2f}\nYour total pay "
      f"is ${total_pay:,.2f}")
