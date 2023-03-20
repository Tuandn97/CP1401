"""
CP1401 2022-3 Assignment 1
Program 2 - Space Cadet
Name: Dao Ngoc Tuan
Date started: December 5th, 2022

Pseudocode:
get practical_score,exam_score
total_score = practical_score + exam_score
if total_score < 50
    result  = "You failed. Please try again next year."
elif practical_score >= exam_score
    result =  "You will become a field agent."
else
    result =  "You will become a desk office."
display total_score and result

if total_score >= 90
display "Congratulations on making the honour roll!"
"""
print("Welcome Trainee Space Cadet. How did you do?")
LOW_THRESHOLD = 0
HIGH_THRESHOLD = 50
PASS_SCORE = 50
MAXIMUM_TOTAL_SCORE = 100
HONOUR_ROLL = 90

practical_score = int(input(f"Practical score ({LOW_THRESHOLD}-{HIGH_THRESHOLD}): "))
exam_score = int(input(f"\t Exam score ({LOW_THRESHOLD}-{HIGH_THRESHOLD}): "))

total_score = practical_score + exam_score

if total_score < PASS_SCORE:
    result = "You failed. Please try again next year."
elif practical_score >= exam_score:
    result = "You will become a field agent."
else:
    result = "You will become a desk office."

print(f"Your total score is {total_score} out of {MAXIMUM_TOTAL_SCORE}. \n{result}")

if total_score >= HONOUR_ROLL:
    print("Congratulations on making the honour roll!")
