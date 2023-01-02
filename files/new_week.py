import os
from 
from workout.files.utility_funcs import write_data


def new_week():
    """
    Function will create new file for the week if new week
    """
    file_path = f"user_details/weigh_in/week_{week_number}.json"
    if not os.path.exists(file_path):
        write_data(week_number, week_data)
    else:
        print("week good")
