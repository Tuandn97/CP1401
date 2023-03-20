# Seconds Display
"""
Pseudocode
function main
    for times in range (0, 3176, 635)
        minutes, seconds = format_minutes_seconds(times)
        display "(time) seconds is (minutes)m (seconds)s"
    get time
    minutes, seconds = format_minutes_seconds(times)
    display "You love (minutes)m (seconds)s"

function format_minutes_seconds(times)
    minutes =  times // 60
    seconds = times % 60
    return minutes, seconds

"""
SECONDS = 60
STARTS = 0
ENDS = 3176
STEPS = 635


def main():
    """ Display random times into minutes and seconds, ask users input the time and display into minutes and seconds"""
    for times in range(STARTS, ENDS, STEPS):
        minutes, seconds = format_minutes_seconds(times)
        print(f"{times} seconds is {minutes}m {seconds}s")

    times = int(input("Favourite duration in seconds: "))
    minutes, seconds = format_minutes_seconds(times)
    print(f"You love {minutes}m {seconds}s ")


def format_minutes_seconds(times):
    """Calculate the minutes, second  from the times"""
    minutes = times // SECONDS
    seconds = times % SECONDS
    return minutes, seconds


main()
