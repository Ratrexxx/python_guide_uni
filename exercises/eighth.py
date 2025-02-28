from utils import get_int_input

def solution():
    total_seconds = get_int_input("Please enter the amount of seconds you want to break down: ", min_value=1)
    
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    
    print(f"{total_seconds} seconds are equivalent to:")
    print(f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds")
    
    if weeks > 0:
        print(f"{weeks} weeks")
    if days > 0:
        print(f"{days} days")
    if hours > 0:
        print(f"{hours} hours")
    if minutes > 0:
        print(f"{minutes} minutes")
    print(f"{seconds} seconds")