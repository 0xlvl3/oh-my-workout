# Libraries.
import os
import json

# Modules.
from workout import Workout
from eset import Eset
from welcome_back import welcome_back
from welcome import welcome
from open_menu import open_menu
from add_workout import add_workouts
from add_store import make_storage


# Workout(date, name, total_weight_lifted, duration  )
# Set(exercise, reps, weight )

# Welcome.

# Check will see if workout_data directory and user_details exist.
# If they do it will welcome that user back.
if os.path.exists("workout_data") and os.path.exists("user_details"):
    GLOBAL_USER = welcome_back()
    print(f"Welcome back {GLOBAL_USER}")
else:
    # If they don't exist it will go through welcome screen.
    GLOBAL_USER = welcome()

# Storage for our workouts.
workouts = {}

open_menu("menu.txt")
# Create menu
# Start workout
# List workouts
# Create new


def main():
    """
    Will be our main loop for our program
    """
    while True:
        print("\n'0' to see the menu again")
        user_navigation = int(input(f"What do you want to do {GLOBAL_USER}\nInput: "))
        if user_navigation == 1:
            make_storage()
        elif user_navigation == 0:
            open_menu("menu.txt")
        else:
            print("Exiting program...")
            exit()


print(f"\nWow you got it working {GLOBAL_USER}")
main()
# workout = Workout("12/12/2022", "Pull", "value_will_be_calc", "120mins")
# print(f"{workout.duration} {workout.name}")
# eset = Eset("Bicep Curl", "20", "20kg")
# print(f"{GLOBAL_USER} did {eset.exercise} for {eset.reps} with {eset.weight}")
