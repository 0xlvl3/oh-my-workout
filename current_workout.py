from workout import Workout
from eset import Eset

import time


def working_out():
    start = time.time()

    while True:
        add_new = input("Add another set? (y/n)").lower()
        if add_new == "y":
            exercise = input("Exercise name: ").lower()
            set_count = int(input("Set number: "))
            reps = int(input("Reps: "))
            weight = int(input("Weight: "))
            print(
                f"Exercise: {exercise} set number {set_count}, for {reps} reps at {weight} weight"
            )
        if add_new == "n":
            break
    end = time.time()

    elapsed = end - start

    print(f"Elapsed time: {elapsed}")


working_out()
