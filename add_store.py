import os


def make_storage():
    """
    Function will create storage for our workouts
    """
    user_input = input(
        f"Hello, do you want to create a new folder for a group of workouts\n(Y/N)"
    ).lower()
    if user_input == "y":
        print("ok")
    else:
        print("returning to menu")
