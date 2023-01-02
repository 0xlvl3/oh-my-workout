import os
import json

from workout.files.utility_funcs import week


def directory_check():
    """
    Function will check to see if weigh_in directory exists
    weigh_in stores week data for user
    """
    if not os.path.exists(f"user_details/weigh_in"):
        print("Creating directories and files")
        week_data = week()
        os.mkdir(f"user_details/weigh_in")
        with open(f"user_details/weigh_in/week_{week_number}.json", "w") as file:
            json.dump(week_data, file, indent=4)
    else:
        print("Directory exists")
