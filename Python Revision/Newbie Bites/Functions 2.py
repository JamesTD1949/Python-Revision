#Objective: Practice using more functions in Python
a = 10
b = 5


def multiply_numbers(a,b):
    return a*b


def enter_name():
    username = input("Please enter your username: ")
    return username

#Expected Result: 50
print(multiply_numbers(a,b))

#Expected Result: user inputted string
print(enter_name())
