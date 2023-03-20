# 4. Read a String from a File
def prac_09():
    in_file = open("name.txt", 'r')
    text = in_file.read()
    in_file.close()
    print(f"Greetings {text}!")


# prac_09()

# 5. Greater-Than Counter
"""
Pseudocode

function question_5
    count_greater = 0
    count_number = 0
    get file_name
    Get threshold
    open file_name  for reading as in_file 
    for number in in_file
        covert number to float number 
        count_number = count_number + 1
        if number > threshold 
            count_greater = count_greater + 1
    close in_file 
    percentage = (count_greater/count_number) * 100
    display count, threshold
        
"""
PERCENTAGE_RATE = 100


def question_5():
    count_greater = 0
    count_number = 0
    file_name = input(f"Filename: ")
    threshold = float(input(f"Threshold: "))
    in_file = open(file_name, 'r')
    for number in in_file:
        number = float(number)
        count_number += 1
        if number > threshold:
            count_greater += 1
    in_file.close()
    percentage = (count_greater/count_number) * PERCENTAGE_RATE
    print(f"Processing...\n{count_greater} out of {count_number} ({percentage:.1f}%) "
          f"values in {file_name} are greater than {threshold}.  ")


# question_5()

# 6. File Filter
"""
Pseudocode
function question_6()
    get in_file_name, out_file_name, search_string
    open in_file_name file for reading as in_file_input
    open out_file_name file for writing  as in_file_output
    for line in in_file_name
        if search_string in line
            write string into out_file_name
    close in_file_name, out_file_name
    
"""


def question_6():
    in_file_name = input("Name of input file: ")
    out_file_name = input("Name of output file: ")
    search_string = input("Search string: ")
    in_file_input = open(in_file_name, 'r')
    in_file_output = open(out_file_name, 'w')
    for line in in_file_input:
        if search_string in line:
            print(line, file=in_file_output)
    in_file_input.close()
    in_file_output.close()


question_6()
