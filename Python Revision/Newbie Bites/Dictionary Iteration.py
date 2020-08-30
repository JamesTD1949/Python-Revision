#Objective: Revise how to loop through a dictionary via a for loop in Python
my_cars = {'Nissan': 2004, 'Jeep': 2013, 'Mazda': 2016, 'Toyota': 2015}


def print_cars(my_cars):
    for make, year in my_cars.items():
        print(f"{make}: {year}")

print_cars(my_cars)
