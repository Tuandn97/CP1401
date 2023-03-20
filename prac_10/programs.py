# 1. Print a line
HYPHENS = 40


def question_1():
    """prints a line of 40 hyphens"""
    print("-" * HYPHENS)


# question_1()

# 2. Is it even?


def question_2():
    """Get number and determine The number is even or odd"""
    some_number = int(input("Number: "))
    if is_even(some_number):
        print(f"{some_number} is even")
    else:
        print(f"{some_number} is odd")


def is_even(some_number):
    """ Check the modulo of the number"""
    return (some_number % 2) == 0


# question_2()

# 3. Get Non-empty String


def question_3():
    """Main program"""
    name = get_valid_string("Name: ")
    birthplace = get_valid_string("Birthplace: ")
    print(f"Hi {name} from {birthplace}")


def get_valid_string(prompt):
    """Get and error_check  the empty string """
    string = input(prompt)
    while string == "":
        print("You can not leave it empty, please enter again!! ")
        string = input(prompt)
    return string


# question_3()


# 4. Number list


def question_4():
    """Get min and max number then display the list from min to max """
    numbers = []
    min_number = int(input(f"Minimum number: "))
    max_number = int(input(f"Maximum number: "))
    while max_number <= min_number:
        print(f"Your maximum must be greater than {min_number}")
        max_number = int(input(f"Maximum number: "))
    for number in range(min_number, max_number+1):
        numbers.append(number)
    print(numbers)


# question_4()


# 5. Subject List


def question_5():
    subject_codes = []
    subject_code = input("Enter subject code: ").upper()
    while subject_code != "":
        if len(subject_code) == 6 and subject_code[0:2].isalpha() and subject_code[2:6].isdigit():
            subject_codes.append(subject_code)
        else:
            print("Invalid subject code")

        subject_code = input("Enter subject code: ").upper()

    print(f"You do these {len(subject_codes)} subjects: ")
    for i in range(len(subject_codes)):
        print(subject_codes[i], sep="")
    if "CP1401" in subject_codes:
        print("You are cool")


question_5()
