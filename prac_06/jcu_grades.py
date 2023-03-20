# JCU_Grades
"""
Algorithm
function main()
    score = get score
    while score > 0
        grades = determine_grades
        display grades
        score = get score
    if score < 0
        get_number_random_score
        random_score

function determine_grades (score)
    if score < 50
        return "F"
    else if score < 65
        return "P"
    else if score < 75
        return "C"
    else if  score < 85
        return "D"
    else return "HD"


function random_score
    for i in range (number_random_score)
        score = random from 0 to 100
        determine_grades
        grades = determine_grades(score)
        display grade
"""
import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
F_SCORE = 50
P_SCORE = 65
C_SCORE = 75
D_SCORE = 85


def main():
    score = float(input("Score: "))
    while score > MINIMUM_SCORE:
        grades = determine_grades(score)
        print(f"The score {score} is {grades}")
        score = float(input("Score: "))
    if score < MINIMUM_SCORE:
        number_random_score = int(input("How many random scores: "))
        random_score(number_random_score)


def determine_grades(score):
    if score < F_SCORE:
        return "F"
    elif score < P_SCORE:
        return "P"
    elif score < C_SCORE:
        return "C"
    elif score < D_SCORE:
        return "D"
    else:
        return "HD"


def random_score(number_random_score):
    for i in range(number_random_score):
        score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
        determine_grades(score)
        grades = determine_grades(score)
        print(f"{score} = {grades}")


def run_test():
    grades = determine_grades(41)
    print(grades)  # it should be "F"
    grades = determine_grades(64)
    print(grades)  # it should be "P"
    grades = determine_grades(74)
    print(grades)  # it should be "c"
    grades = determine_grades(84)
    print(grades)  # it should be "D"
    grades = determine_grades(86)
    print(grades)  # it should be "HD"


# run_test()
main()
