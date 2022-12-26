from workout import Workout
from add_workout import add_workouts

# Check to see if user is already a user
# if they aren't a user go through this
GLOBAL_USER = input("Hello welcome, what is your name? ").lower()
print(f"{GLOBAL_USER} welcome")


# storage for our workouts
workouts = {}
