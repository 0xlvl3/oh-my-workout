# Libraries
import os

# Modules.
from workout import Workout
from eset import Eset
from welcome import welcome
from add_workout import add_workouts


# Workout(date, name, total_weight_lifted, duration  )
# Set(exercise, reps, weight )

# Check to see if user is already a user
# if they aren't a user go through this
if os.path.exists("workout_data"):
    with open("workout_data/username.json", "r") as file:
        GLOBAL_USER = file.read()
    print(f"Welcome back {GLOBAL_USER}")
else:
    GLOBAL_USER = welcome()

# GLOBAL_USER = welcome()

# storage for our workouts
workouts = {}

print(f"\nWow you got it working {GLOBAL_USER}")
# workout = Workout("12/12/2022", "Pull", "value_will_be_calc", "120mins")
# print(f"{workout.duration} {workout.name}")
# eset = Eset("Bicep Curl", "20", "20kg")
# print(f"{GLOBAL_USER} did {eset.exercise} for {eset.reps} with {eset.weight}")
