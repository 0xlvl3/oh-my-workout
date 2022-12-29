import json
import datetime
import calendar

# Prompt to enter weigh in
# Check list of weigh ins
# Give median of current week
# Show graph showing weigh ins
# Create a dictionary that saves an id and weigh as a 7 day dictionary

# Get current date and time
now = datetime.datetime.now()

# Use datetime now, in calendar.weekday func to get day as 0 index
day_of_week = calendar.weekday(now.year, now.month, now.day)
print(day_of_week)

# get the current day until we move onto the next week
next_week_start = now + datetime.timedelta(days=(7 - day_of_week))
print(next_week_start)

# use now again to return the number of the week of the year
week_number = now.isocalendar()[1]

# strftime method will formate current date and time to str
print(f"Current date: {now.strftime('%Y-%m-%d')}")
print(f"Next week start: {next_week_start.strftime('%Y-%m-%d')}")
print(f"Week number is: {week_number}")

week_data = {
    "Monday": 0,
    "Tuesday": 0,
    "Wednesday": 0,
    "Thursday": 0,
    "Friday": 0,
    "Saturday": 0,
    "Sunday": 0,
}


def daily_weigh():
    print("lol")


def weigh_in():
    menu = """
1 ) Daily weigh in
2 ) Show weekly stats 
3 ) Give median for week 
4 ) Show graph view
5 ) Exit to menu
          """
    print(menu)
    while True:
        user_choice = input(
            """
To see the menu again enter '0'
Navigate to:    """
        )
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice == 0:
                print(menu)
            elif user_choice == 1:
                print("\nDaily weigh in")
            elif user_choice == 2:
                print("\nShow weekly stats")
            elif user_choice == 3:
                print("\nGive median for week")
            elif user_choice == 4:
                print("\nShow graph view")
            elif user_choice == 5:
                break
        else:
            print("\n### Please select an option from the menu (0 - 5)")


weigh_in()
