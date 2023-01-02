import json
import os
import datetime
import calendar
import matplotlib.pyplot as plt

# Prompt to enter weigh in
# Check list of weigh ins
# Give median of current week
# Show graph showing weigh ins
# Create a dictionary that saves an id and weigh as a 7 day dictionary

menu = """
1 ) Daily weigh in
2 ) Show weekly stats
3 ) Give median for week
4 ) Show graph view
5 ) Exit to menu
"""

# Used in multiple areas.
# Returns current datetime.
now = datetime.datetime.now()


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


# Storing for use.
day_of_week = get_day()

# Get the current day until we move onto the next week.
next_week_start = now + datetime.timedelta(days=(7 - day_of_week))
# print(next_week_start)

# Use now again to return the number of the week of the year.
week_number = now.isocalendar()[1]

# strftime method will formate current date and time to str
# print(f"Current date: {now.strftime('%Y-%m-%d')}")
# print(f"Next week start: {next_week_start.strftime('%Y-%m-%d')}")
# print(f"Week number is: {week_number}")

# Week data that gets stored in JSON.
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


def directory_check():
    """
    Function will check to see if weigh_in directory exists
    weigh_in stores week data for user
    """
    if not os.path.exists(f"user_details/weigh_in"):
        print("Creating directories and files")
        os.mkdir(f"user_details/weigh_in")
        with open(f"user_details/weigh_in/week_{week_number}.json", "w") as file:
            json.dump(week_data, file, indent=4)
    else:
        print("Directory exists")


# def directory_week_number():
#   """
#  Function will parse the week number from the current week file path,
# used for comparison
# """
# current_week_file = f"user_details/weigh_in/week_{week_number}.json"
# current_week_comparison = current_week_file.split("_")[3].split(".json")[0]
# print(current_week_comparison)
# print(current_week_file)
# current_week_comparison = int(current_week_comparison)
# return current_week_comparison


def new_week():
    """
    Function will create new file for the week if new week
    """
    file_path = f"user_details/weigh_in/week_{week_number}.json"
    if not os.path.exists(file_path):
        write_data(week_number, week_data)
    else:
        print("week good")


new_week()


# def week_check(current_week_comparison):
#    """
#    Function compares current week to current week file, if equal
#    no file will be created, if it isn't new week will be created
#    """

# Compare week in file name if not the same make new week file.
#    if week_number != current_week_comparison:
#        print("Creating new week file")

# Create new week file.
#        with open(f"user_details/weigh_in/week_{week_number}.json", "w") as file:
#            json.dump(week_data, file, indent=4)
#    else:
#        print(f"We are still in week {week_number}")


# Check if directory exists.
# directory_check()

# Storing week number in comparison variable.
# current_week_comparison = directory_week_number()
# print(current_week_comparison)
# Compare week in file name if not the same make new week file.
# week_check(current_week_comparison)


# Will take in daily weight; once input is in for the day it won't ask again.
# Possible ask in the menu to set weigh in again for the day ?
def daily_weigh():
    """
    Function will take a daily weigh in using the switch below to
    determine if user has already weighed in; if they have will
    return to menu
    """
    # Daily weigh in if not type weigh if they have tell them they have.
    def switch(day_of_week):
        """
        Function is python version of a switch statement used
        to compare week day int with days of the week in week data
        """
        if day_of_week == 0:
            # print("Monday")
            return "Monday"
        elif day_of_week == 1:
            # print("Tuesday")
            return "Tuesday"
        elif day_of_week == 2:
            # print("Wednesday")
            return "Wednesday"
        elif day_of_week == 3:
            # print("Thursday")
            return "Thursday"
        elif day_of_week == 4:
            # print("Friday")
            return "Friday"
        elif day_of_week == 5:
            # print("Saturday")
            return "Saturday"
        elif day_of_week == 6:
            # print("Sunday")
            return "Sunday"
        else:
            print("Error")

    # Switch statement.
    day = switch(day_of_week)

    # Open JSON store in data
    data = open_week(week_number)

    # If weigh not done.
    value = data[day]
    if value == 0:
        daily = input("What are you weighing in at this morning: ")
        data[day] = daily
        write_data(week_number, data)

    elif value != 0:
        user_input = input(
            f"""
Do you want to update your daily weigh in at {value}
(Y/N): """
        ).lower()
        if user_input == "y":
            daily = input("What are you weighing in at this morning: ")
            data[day] = daily
            write_data(week_number, data)
        else:
            print("\n### You already weighed in today, returning to menu.")
            print(menu)

    # Return to menu.
    else:
        print("\n### You already weighed in today, returning to menu.")
        print(menu)


# Show weigh in statistics
def weekly_stats():
    """
    Function will return a list of the current weekly weigh ins.
    """
    data = open_week(week_number)

    print(f"\nWeekly statistics for week {week_number}")
    print("-----------------------------")
    for key, value in data.items():
        print(f"{key}: {value}")
    print("-----------------------------")


def get_median(data):
    """
    Function will return median for the week to the user.
    """
    week_total = 0
    for value in data.values():
        value = float(value)
        print(value)
        week_total = value + week_total
    print(f"\nWeigh in total: {week_total}")
    median = round(week_total / 7.0, 2)
    print(f"Your median for the week is: {median}")


# Give median for week depending on data.
def weekly_median():
    """
    Function will give weekly median depending on user input.
    """

    # Data used.
    data = open_week(week_number)

    while True:
        navigate_to = input(
            """
1 ) See current week median
2 ) See a specific week median
3 ) Exit to menu
Navigate to: """
        )

        if navigate_to.isdigit():
            navigate_to = int(navigate_to)
            if navigate_to == 1:
                get_median(data)
            elif navigate_to == 2:
                week_choice = input("Write the week number you wish to see: ")
                int(week_choice)
                data = open_week(week_choice)
                get_median(data)
            else:
                print(menu)
                break


def graph_view():
    """
    Function will return a graph depending on which week the user picks.
    """
    # Days in week
    x = [1, 2, 3, 4, 5, 6, 7]
    y = []
    # Ask user what week to see
    user_choice = input(f"Place a week you want to see: ")
    data = open_week(user_choice)
    for value in data.values():
        value = str(value)
        y.append(value)

    fig, ax = plt.subplots()
    # plt.figure(
    #   facecolor="#bd91e4",
    # )
    ax.scatter(x, y, color="blue", marker="o")
    ax.set_title(f"Week {user_choice}")
    ax.set_xlabel("Week days")
    ax.set_ylabel("Weigh in")
    ax.set_facecolor("#fff2cc")
    ax.tick_params(color="#4a86cb", labelcolor="#4a86cb")

    for spine in ax.spines.values():
        spine.set_edgecolor("#5272bf")
    plt.show()


# Main loop.
def weigh_in():
    """
    Function is the main loop for this set of functions.
    """
    print(menu)
    while True:
        user_choice = input(
            """
To see the menu again enter '0'
Navigate to: """
        )
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice == 0:
                print(menu)
            elif user_choice == 1:
                daily_weigh()
            elif user_choice == 2:
                weekly_stats()
            elif user_choice == 3:
                weekly_median()
            elif user_choice == 4:
                graph_view()
            elif user_choice == 5:
                break
        else:
            print("\n### Please select an option from the menu (0 - 5)")


weigh_in()
