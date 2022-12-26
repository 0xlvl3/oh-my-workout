import os
import json

# Will run if user hasn't ran program before.


def welcome():
    """
    Function will create a global user for the program
    and also a directory called workout_data for their
    workout directories and data
    """
    GLOBAL_USER = input(
        f"Hello welcome to 'Oh-my-workout', what is your name user? "
    ).lower()

    print(f"Welcome {GLOBAL_USER} creating your workout_data directory now..")
    # Creates directory for data
    os.mkdir("workout_data")
    # Saves username
    if os.path.exists:

        name = json.dumps({"username": GLOBAL_USER})
        with open("workout_data/username.json", "w") as file:
            file.write(name)
    else:
        print("error")

    print(f"\nDirectory has been made {GLOBAL_USER}")
    return GLOBAL_USER
