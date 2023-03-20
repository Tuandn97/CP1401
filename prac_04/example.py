"""
Algorithm
get birth_month
while birth_month < 0 or birth_month > 12
    display Invalid month
    get birth_month
for count in range from 1 to birth_month + 1
    display count
if birth_month <= 6
    message = ("Your birth month is the first half of the year")
else
    message = ("Your birth month is the second half of the year")
display message
"""

MINIMUM_MONTH = 1
MAXIMUM_MONTH = 12
HALF_YEAR = MAXIMUM_MONTH / 2
birth_month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))
while birth_month < MINIMUM_MONTH or birth_month > MAXIMUM_MONTH:
    print("Invalid month")
    birth_month = int(input("Enter your birth month: "))

for count in range(1, birth_month + 1):
    print(count, end=" ")
print()

if birth_month <= HALF_YEAR:
    message = ("Your birth month is the first half of the year")
else:
    message = ("Your birth month is the second half of the year")

print(message)


