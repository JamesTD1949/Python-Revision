#Objective: Revise working with tuples in Python
car_brands = ['Mazda', 'McLaren', 'Opel', 'Toyota', 'Honda']


def convert_to_tuple(car_brands):
    static_cars = tuple(car_brands)
    return static_cars

print(convert_to_tuple(car_brands))
