# 1. Discount Price

"""
Algorithm
get original_price
discount = original_price * 0.2
new_price = original_price – discount
print new_price
"""

original_price = float(input("Enter your original price:$ "))
DISCOUNT_RATE = 0.2
discount_value = original_price * DISCOUNT_RATE
new_price = original_price - discount_value
print("This is your price after apply the discount:$", new_price, sep="")


# 2. Kilometres to Miles

""""
Algorithm
get distance_in_kilometers
distance_in_miles = distance_in_kilometers * 0.621371
display distance_in_miles
"""

distance_in_kilometers = float(input("Please enter the distance in Kilometers:"))
CONVERSION_RATE = 0.621371
distance_in_miles = distance_in_kilometers * CONVERSION_RATE
print("The distance in miles will be: ", distance_in_miles, sep="" )

# 3. Holiday Cost

"""
Algorithm
get daily_food_cost, daily_activities_cost, number_of_days
total_trip_cost = (daily_hotel_cost + daily_food_cost + daily_activities_cost) * number_of_days
display number_of_days and total_trip_cost

"""
daily_food_cost = float(input("Daily food cost:$"))
daily_activities_cost = float(input("Daily activities cost:$"))
number_of_days = int(input("Number of days:"))
DAILY_HOTEL_COST = 75
total_trip_cost = (daily_food_cost + daily_activities_cost + DAILY_HOTEL_COST) * number_of_days

print("")
print("Total trip cost:$", total_trip_cost, sep="")

# 4. Deep Sleep Calculation (Percentage)

"""
Algorithm
get total_sleep_in_seconds, deep_sleep_in_seconds
percentage = deep_sleep_in_seconds  / total_sleep_in_seconds * 100
deep_sleep_minutes = deep_sleep_in_seconds // 60
deep_sleep_seconds = deep_sleep_in_seconds % 60
total_sleep_minutes = total_sleep_in_seconds // 60
total_sleep_seconds = total_sleep_in_seconds % 60

display  deep_sleep_minutes"m" deep_sleep_seconds"s", total_sleep_minutes"m" total_sleep_seconds"s", percentage

"""
total_sleep_in_seconds = int(input("Total sleep in seconds: "))
deep_sleep_in_seconds = int(input("Deep sleep in seconds: "))

SECONDS = 60
PERCENTAGE = 100

total_sleep_minutes = total_sleep_in_seconds // SECONDS
total_sleep_seconds = total_sleep_in_seconds % SECONDS

deep_sleep_minutes = deep_sleep_in_seconds //SECONDS
deep_sleep_seconds = deep_sleep_in_seconds % SECONDS

percentage = deep_sleep_in_seconds / total_sleep_in_seconds * PERCENTAGE

print("")
print("Deep sleep: ", deep_sleep_minutes, " m ",deep_sleep_seconds, "s" ,sep="")
print("Total sleep: ", total_sleep_minutes, " m ",total_sleep_seconds, "s",  sep="")
print("Percentage: ", percentage, "%", sep="")



