# 1. Percentage program (I, P, O)
"""
Algorithm
get original_value, change
result = original_value * change + original_value
display result
"""
original_value = float(input("Original: "))
change = float(input("Change: "))
result = original_value + original_value * change
print(f"Result: {result}")
# 2. Time of day (decision)
"""
Let time_of_day,user_action
while time_of_day < 0 or time_of_day >23
    display Invalid input
    get time_of_day
if time_of_day < 12 
    message_for_time = "before"
else message_for_time = "after"
if user_action is "coming"
     message_for_action = "coming. Hi!"
else message_for_action =  "going. Bye!"
display It is message_for_time noon and you are message_for_action
"""
SOONEST_TIME = 0
LATEST_TIME = 23
MOON_TIME = 12

time_of_day = int(input(f"Enter the time of day ({SOONEST_TIME} - {LATEST_TIME}):  "))
user_action = input("Are you going or coming: ").lower()
if time_of_day < MOON_TIME:
    message_for_time = "before"
else:
    message_for_time = "after"
if user_action == "coming":
    message_for_action = "coming. Hi!"
else:
    message_for_action = "going. Bye!"

print(f"It is {message_for_time} noon and you are {message_for_action}")

# 3. Coffee orders (Decision)
"""
Algorithm
Get coffee_type, cup_size
if cup_size is small
    cost = 3
elif cup_size is medium
    cost = 4
else
    cost = 5
if coffee_type is not black
    cost = cost + 1
display cost
"""
SMALL_CUP = 3
MEDIUM_CUP = 4
LARGE_CUP = 5
ADD_MILK = 1  # to make white coffee
S = "small"
M = "medium"
B = "black"

coffee_type = input("Black or White coffee: ").lower()
cup_size = input("Size: Small , Medium, or Large: ").lower()
if cup_size == S:
    cost = SMALL_CUP
elif cup_size == M:
    cost = MEDIUM_CUP
else:
    cost = LARGE_CUP
if coffee_type != B:
    cost += ADD_MILK

print(f"Your cost is :${cost}")

# 4. Coffee orders with error-checking (Repetition)
"""
Algorithm
get coffee_type
while coffee_type is not Black and White
    display Invalid choice
    get coffee_type
get cup_size
while cup_size is not small medium large
    display Invalid choice
    get cup_size
if cup_size is small
    cost = 3
elif cup_size is medium
    cost = 4
else
    cost = 5
if coffee_type is while
    cost = cost + 1
display cost
"""
SMALL_CUP = 3
MEDIUM_CUP = 4
LARGE_CUP = 5
ADD_MILK = 1  # to make white coffee
S = "small"
M = "medium"
L = "large"
B = "black"
W = "white"
ERROR_MESSAGE = "Invalid choice"

coffee_type = input("Black or White coffee: ").lower()
while coffee_type != B and W:
    print(ERROR_MESSAGE)
    coffee_type = input("Black or White coffee: ").lower()

cup_size = input("Size: Small , Medium, or Large: ").lower()
while cup_size != S and M and L:
    print(ERROR_MESSAGE)
    cup_size = input("Size: Small , Medium, or Large: ").lower()

if cup_size == S:
    cost = SMALL_CUP
elif cup_size == M:
    cost = MEDIUM_CUP
else:
    cost = LARGE_CUP
if coffee_type == W:
    cost += ADD_MILK
print(f"Your cost is :${cost}")

# 5. Accumulation (Repetition)
"""
total = 0
get low_value, high_value
while high_value <= low_value
    display High value have to be higher than Low value. Please try again!
    get high_value
for i in range from low_value to high_value + 1
    display i
    total = total + i
display total
"""
total = 0
ONE = 1
low_value = int(input("Enter a low value: "))
high_value = int(input("Enter a high value: "))
while high_value < low_value:
    print("High value have to be higher than Low value. Please try again!")
    high_value = int(input("Enter a high value: "))
for i in range(low_value, high_value + ONE):  # + ONE: to display and add the last number
    print(i, end=" ")
    total += i
print(f"Total: {total}")
