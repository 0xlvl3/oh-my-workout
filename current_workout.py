from workout import Workout
from eset import Eset

import time
from datetime import date
import datetime
import json
import os


def working_out():
    start = time.time()
    now = datetime.datetime.now()
    formatted_time = now.strftime("%I:%M:%S_%p")
    print(formatted_time)
    current_date = date.today()

    workout_name = input("Name your workout: ").lower()
    # Check if directory exists
    if not os.path.exists(f"workout_data/{workout_name}"):
        os.mkdir(f"workout_data/{workout_name}")
        with open(
            f"workout_data/{workout_name}/workout_{current_date}_{formatted_time}.json",
            "w",
        ) as file:
            workout = {}
            json.dump(workout, file)
    elif os.path.exists(f"workout_data/{workout_name}"):
        with open(
            f"workout_data/{workout_name}/workout_{current_date}_{formatted_time}.json",
            "w",
        ) as file:
            workout = {}
            json.dump(workout, file)

    print("Workout starting..")
    time.sleep(1)
    print("Workout starting...")
    time.sleep(1)
    print("Workout starting....")
    print(f"{current_date}")

    with open(
        f"workout_data/{workout_name}/workout_{current_date}_{formatted_time}.json",
        "a",
    ) as f:
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

                add_set = Eset(exercise, set_count, reps, weight)

                # Serialize the object using json.dump function
                add_set_data = json.dumps(add_set.__dict__, indent=4)
                print(f"{add_set} added")

                f.write(add_set_data)

            elif add_new == "n":
                break

        end = time.time()

        elapsed = end - start

        print(f"Elapsed time: {elapsed}")


working_out()
