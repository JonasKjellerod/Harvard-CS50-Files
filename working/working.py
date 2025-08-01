import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Define a regular expression pattern to match the 12-hour time format
    pattern = re.compile(r'(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)')

    # Search for the pattern in the input string
    match = pattern.match(s)

    # If no match is found, raise a ValueError
    if not match:
        raise ValueError("Invalid time format")

    # Extract the components of the time
    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    # Convert the components to integers
    start_hour = int(start_hour)
    start_minute = int(start_minute) if start_minute else 0
    end_hour = int(end_hour)
    end_minute = int(end_minute) if end_minute else 0

    # Validate the time components
    if not (1 <= start_hour <= 12) or not (0 <= start_minute < 60):
        raise ValueError("Invalid start time")
    if not (1 <= end_hour <= 12) or not (0 <= end_minute < 60):
        raise ValueError("Invalid end time")

    # Convert the start time to 24-hour format
    if start_period == "PM" and start_hour != 12:
        start_hour += 12
    elif start_period == "AM" and start_hour == 12:
        start_hour = 0

    # Convert the end time to 24-hour format
    if end_period == "PM" and end_hour != 12:
        end_hour += 12
    elif end_period == "AM" and end_hour == 12:
        end_hour = 0

    # Format the times in 24-hour format
    start_time = f"{start_hour:02}:{start_minute:02}"
    end_time = f"{end_hour:02}:{end_minute:02}"

    return f"{start_time} to {end_time}"

if __name__ == "__main__":
    main()
