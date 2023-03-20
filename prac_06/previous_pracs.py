# Calculate salary for worker level
"""
Algorithm

function main
    worker_level = get_valid_number(prompt, 1, 10)
    salary = calculate_salary(5000, worker_level)
    display worker_level, salary


function get_valid_number(prompt, low, high)
    get number
    while number < low or number > high
        display Invalid input
        get number
    return number


function calculate_salary(worker_level):
    return 5000 * worker_level

Call main
"""
BASE_SALARY = 5000
MINIMUM_SALARY_LEVEL = 1
MAXIMUM_SALARY_LEVEL = 10


def main():
    worker_level = get_valid_level("Worker level: ", MINIMUM_SALARY_LEVEL, MAXIMUM_SALARY_LEVEL)
    salary = calculate_salary(BASE_SALARY, worker_level)
    print(f"With worker level {worker_level}, your salary is ${salary:,.2f}")


def get_valid_level(prompt, low, high):
    number = int(input(prompt))
    while number < low or number > high:
        print("Invalid worker level")
        number = float(input(prompt))
    return number


def calculate_salary(base_salary, worker_level):
    return base_salary * worker_level


main()

# Nested Loops
"""
Algorithm

function main 
    get rows,columns
    draw_grid
function draw_grid(Rows,Columns)
    for row_counter in range 0 - Rows
        for columns_counter in range 0 - Columns
            display columns_counter
        display ()

call main
"""


def main():
    rows = int(input("Rows: "))
    columns = int(input("Columns: "))
    draw_grip(rows, columns)


def draw_grip(rows, columns):
    for row_counter in range(rows):
        for columns_counter in range(columns):
            print(columns_counter, end=" ")
        print()


main()
