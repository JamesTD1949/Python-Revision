#Objective: Revise using the less than and greater than symbols in python

def speed_check(speed):
    if speed > 100:
        print("Please slow down.")
    elif speed < 80:
        print("Please speed up.")
    else:
        print("Thanks for driving safely!")

#Expected Result: "Please slow down."
speed_check(101)
#Expected Result: "Please speed up."
speed_check(79)
#Expected Result: "Thanks for driving safely!"
speed_check(81)
