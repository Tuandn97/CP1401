#  Hours
SECONDS = 60
HOURS = 3600
STARTS = 0
ENDS = 47529
STEPS = 3634


def main():
    for times in range(STARTS, ENDS, STEPS):
        minutes = format_minutes(times)
        seconds = format_seconds(times)
        hours = format_hours(times)
        print(f"{times} seconds is {hours:2}h {minutes:2}m {seconds:2}s")

    times = int(input("Favourite duration in seconds: "))
    minutes = format_minutes(times)
    seconds = format_seconds(times)
    print(f"You love {minutes}m {seconds}s ")


def format_minutes(times):
    """Calculate the minutes from the times"""
    minutes = times // SECONDS
    return minutes


def format_seconds(times):
    """Calculate the second  from the times"""
    seconds = times % SECONDS
    return seconds


def format_hours(times):
    """Calculate the hours  from the times"""
    hours = times // HOURS
    return hours


main()
