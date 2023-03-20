"""CP1401 - Practical 7 - Debugging.
The "demo" problem shows how the answers should be written.
Follow the example and template to answer the questions (find and fix problems) below.
"""


def demo():
    """Problematically do list duplication and reversing."""
    things = [1, 2, 3, 4]
    new_things = dupli_reversify(things)
    print(new_things)
def dupli_reversify(x):
    """Create mirrored list from passed-in list, e.g., [0, 1] -> [0, 1, 1, 0]."""
    return x + x.reverse()

# Problem(s) for demo program:
# x.reverse() modifies the list in-place and evaluates to None (it does not evaluate to a list).
# x (list) + None gives a TypeError
# (Notice that the answer is about the bug/problem, not about style, names, formatting, etc.)

# Fixed code for demo program:
def dupli_reversify(x):
    """Create mirrored list from passed-in list, e.g., [0, 1] -> [0, 1, 1, 0]."""
    return x[:] + x[::-1]
    # or
    # return x + list(reversed(x))
# (Notice that the answer includes the whole fixed function. No style/naming issues have been improved.)

# Questions start here:

def main_1():
    """Determine the parity of a user's number."""
    number = int(input("Enter number: "))
    parity = calculate_parity
    print(parity)

def calculate_parity(number):
    """Calculate the parity (0 or 1) of number passed in."""
    return (number%2)

# Problem(s) for program 1:
# line 34 - missed the argument

# Fixed code for program 1:
# parity = calculate_parity(number)

def main_2():
    """Print numbers from 0 up to the user's input multiplied by 2."""
    # E.g., if input is 12, should print 0 2 4 6 8 10 12 14 16 18 20 22 24
    numnums = input("How many: ")
    for i in numnums:
        print(i * 2)

# Problem(s) for program 2:
# line 50 - did not convert from string to integer
# line 50 - variable mane not clear
# line 51 52 - Login error: it just printed the result of i*2

# Fixed code for program 2:
#  numbers = int(input("How many: "))
#  for i in range(0, (numbers*2) + 1, 2):
#     print(i, end=" ")

def main_3():
    """Determine the area of a rectangle."""
    length, width = 12, 10
    area = calculate_area(length, width)
    print(f"The area is {area}")

def calculate_area(l, w):
    """Calculate the area of a rectangle from its dimensions."""
    result = l * w
    print(result)

# Problem(s) for program 3:
# line 71 - it is not print, we already have print in the main function, we have to return the value the to the main function

# Fixed code for program 3:
# line 71 - return(result)

def main_4():
    """Show how old a person will be in the future."""
    increment = 10
    age = int(input("Age: "))
    while age < 0 and age > 120:
        print("Invalid age")
        age = int(input("Age: "))
    print(f"In {increment} years, you will be {age} years old!")

# Problem(s) for program 4:
# line 83 -  Naming - It is a constant, so it have to naming in all caps
# line 85 - Wrong range of condition - check outside range, so i have to be or not and
# Did not have a code to calculate to age after 10 year
# line 88 - logic error -  we have to print the new age( age after 10 years) instead of age

# Fixed code for program 4:
# line 83: INCREMENT  = 10
# line 85: while age < 0 or age > 120:
# add more code: new_age  = age + INCREMENT
# line 88: print(f"In {INCREMENT} years, you will be {new_age} years old!")

# demo()
# main_1()
# main_2()  # Note: these are not good names; just something to reduce the amount of copying we need to do
# main_3()
# main_4()