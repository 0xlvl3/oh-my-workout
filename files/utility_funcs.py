import datetime
import calendar
import json

# File contains functions that are used within my other main functions


def week():
    week_data = {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0,
    }
    return week_data


def get_day():
    """
    Function returns current day of the week, zero-indexed
    0-6
    """
    # Get current date and time.
    now = datetime.datetime.now()

    # Use datetime now, in calendar.weekday func to get day as 0 index.
    day_of_week = calendar.weekday(now.year, now.month, now.day)
    print(day_of_week)
    return int(day_of_week)


def write_data(week_number, data):
    """
    Function will write data to specified week number
    """
    with open(f"user_details/weigh_in/week_{week_number}.json", "w") as file:
        json.dump(data, file, indent=4)


# Will open file replace this in other areas later
def open_week(week_number):
    """
    Function will open specified week number
    """
    with open(f"user_details/weigh_in/week_{week_number}.json") as file:
        data = json.load(file)
        return data
