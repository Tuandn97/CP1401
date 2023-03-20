# 1. Processing Strings

def question_1():
    data_strings = ["Result = 95%", "Final Score = 8%", "Relative Value = 178%",
                    "Something else that's very important = 9.2%", "x = 42%"]
    for data_string in data_strings:
        print(float(data_string[data_string.find("=") + 2:len(data_string) - 1]))


# question_1()

# 2. Date strings

THIS_YEAR = 2022


def question_2():
    birthday = input(f"DOB: ")
    birthday_split = birthday.split("/")
    year_of_birth = int(birthday_split[2])
    age = THIS_YEAR - year_of_birth
    next_year_age = age + 1  # add 1 year
    next_year = THIS_YEAR + 1  # add 1 year
    print(f"You were born in {year_of_birth}"
          f"\nYou will turn in {next_year_age} in {next_year}")


# question_3()

# 3. Subject Code Strings
"""
Pseudocode
function question_3()
    get subject_code
    while subject_code is not empty string
        discipline = subject_code[0:2]
        year_level = int(subject_code[2])
        it_string = determine_it_subject(discipline)
        year_string =  determine_year_level(year_level)
        display year_string, it_string

function determine_it_subject(discipline)
    if discipline is "CP"
        return "IT"
    else return ""
    


function determine_year_level(year_level)
    if year_level == 1
        year_string = "first_year"
    else if  year_level == 2
        year_string  = "second_year"
    else if year_level == 3
        year_string = "third_year"
    else 
        year_string = "Master or other"
    return year_string
"""
FIRST_YEAR = 1
SECOND_YEAR = 2
THIRD_YEAR = 3


def question_3():
    """ The main function of the program """
    subject_code = input(f"Enter subject code: ")
    while subject_code != "":
        discipline = subject_code[0:2].upper()  # take 2 first index element
        year_level = int(subject_code[2])   # take the third index element
        it_string = determine_it_subject(discipline)
        year_string = determine_year_level(year_level)
        print(f"That is a {year_string}{it_string} subject.")
        subject_code = input(f"Enter subject code: ")


def determine_it_subject(discipline):
    """ Determine which subject is IT subject, based on discipline """
    if discipline == "CP":
        return "IT"
    else:
        return ""


def determine_year_level(year_level):
    """ Determine year_level based on the third index of the subject code """
    if year_level == 1:
        return "first_year "
    elif year_level == 2:
        return "second_year "
    elif year_level == 3:
        return "third_year "
    else:
        return "Master or other "


question_3()
