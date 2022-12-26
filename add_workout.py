from workout import Workout


def add_workouts():
    date = input("Enter the date: ")
    exercise = input("Enter the exercise name: ")
    sets = input("Enter the number of sets: ")
    reps = input("Enter the number of reps: ")
    weight = input("Enter weight: ")
    workout = Workout(date, exercise, sets, reps, weight)
    return workout
