#Objective: Revise using an infinite loop to take in user input until they terminate the loop
VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check: 
       - if 'quit' was entered for color, print 'bye' and break. 
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    while True:
        colour = input("Please enter a colour: ").lower()
        if colour == "quit":
            print("bye")
            break
        else:
            for item in VALID_COLORS:
                exists = False
                if item == colour:
                    exists = True
                    break
            if exists == True:
                print(colour)
            else:
                print("Not a valid color")
                

print_colors()
