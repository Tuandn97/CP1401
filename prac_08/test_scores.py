# test_scores
"""
Algorithm
function  main():
    scores = empty list [0, 100, 130, 0]
    for i in range from 1 to 5
        score = get_valid_score("Score : ", 0, 100)
        add score to scores
    for i in range length of the scores
        score = scores[i]
        grade = determine_grades(scores[i])
        display score and grade
    average_score = calculate_average_score(scores)
    display the average_score
    trend = determine_trend(scores, average_score)
    display the trend

function get_valid_score(prompt, low, high)
    get number
    while number < low or number > high
        print("Invalid Score")
        get number
    return number

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

function calculate_average_score(scores)
    return the sum of scores / length of scores

function determine_trend(scores, average_score)
    if scores[-1] > average_score
        return "positive"
    else return "not positive"

"""

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
START_NUMBER = 1
END_NUMBER = 5
F_SCORE = 50
P_SCORE = 65
C_SCORE = 75
D_SCORE = 85


def main():
    """ Loop and get list, calculate the grade base on the list, and determine the trend"""
    scores = []
    for i in range(START_NUMBER, END_NUMBER):
        score = get_valid_score(f"Score {i}: ", MINIMUM_SCORE, MAXIMUM_SCORE)
        scores.append(score)
    for i in range(len(scores)):
        score = scores[i]
        grade = determine_grades(scores[i])
        print(f"Score {i+1}: {score}, which is {grade}")
    average_score = calculate_average_score(scores)
    print(f"The average score was {average_score:,.3f}")
    trend = determine_trend(scores, average_score)
    print(f"The trend is {trend}")


def determine_grades(score):
    """Determine the grade base on the score"""
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


def get_valid_score(prompt, low, high):
    """ Get the user input and determine the valid score"""
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid Score")
        number = float(input(prompt))
    return number


def calculate_average_score(scores):
    """Calculate the score base on the score in the list"""
    return sum(scores) / len(scores)


def determine_trend(scores, average_score):
    """Determine the trend base on the last index and the average_number """
    if scores[-1] > average_score:
        return f"positive"
    else:
        return f"not positive"


def run_test():
    """Test all cases off the determine_grade function"""
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
