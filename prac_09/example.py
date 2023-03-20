"""total = 0.0
count = 0
open "scores.txt" for reading as in_file
for line in in_file
    score = line as float
    total = total + score
    count = count + 1
close in_file
average = total / count
print average
"""
total = 0.0
count = 0
name = "scores.txt"
# name = input(f"Enter the name of the file: ")
in_file = open(name, 'r')
for line in in_file:
    score = float(line)
    total += score
    count += 1
    print(f"Score = {score:.1f}\tTotal so far = {total:.1f}")
in_file.close()
average = total / count
print(f"Average = {average:.1f}")
