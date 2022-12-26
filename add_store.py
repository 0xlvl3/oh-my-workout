import os


def make_storage():
    """
    Function will create storage for our workouts
    """
    user_storage = input(
        f"Hello, {GLOBAL_NAME} do you want to create a new folder for a group of workouts"
    ).lower()
