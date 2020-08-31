#Objective: Combine f Strings, constant and variables to print to screen if user is old enough to drive
MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    if age >= MIN_DRIVING_AGE:
        print(f"{name} is allowed to drive")
    else:
        print(f"{name} is not allowed to drive")
