"""CP1401 - Practical 8 - Debugging."""

# Debug program 1 - friends' names
names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")
for i in range(1, len(names)):
    print(f"{i}. {names[i]}")
last_number = len(names)
print(f"The last name (number {last_number}) is {names[last_number]}")

# Problem(s) for program 1:
# line 6: If the range from 1 it will skip the index 1 "Abby"
# line 7: if print (i) here, i will start from 0
# line 9: names[last_number] is not the last index in the list, it will display out of range error

# Fixed code for program 1:
# line 6: for i in range(len(names)):
# line 7: print(f"{i+1}. {names[i]}")
# line 9: print(f"The last name (number {last_number}) is {names[-1]}")

# Debug program 2 - title-casing country names
countries = ("australia", "new zeaLAND", "India")
for i in range(len(countries)):
    countries[i] = countries[i].title()
print(countries)  # country names should be in title-case now

# Problem(s) for program 2:
# line 22: Tuple is a fixed list, can not edit the value in the list

# Fixed code for program 2:
# line 22: countries = ["australia", "new zeaLAND", "India"]
