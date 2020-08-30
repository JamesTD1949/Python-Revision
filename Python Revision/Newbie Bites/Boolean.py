#Objective: Revise using Boolean values in python to check if an object is empty

def get_username():
    username = input("Please enter your username: ")
    return username


def print_username(username):
    if username:
        print("Your username is: " + username + ".")
    else:
        print("Sorry, no username was defined.")

#Expected Result: "Your username is name."
print_username("name")
#Expected Result: "Sorry, no username was defined."
print_username("")
