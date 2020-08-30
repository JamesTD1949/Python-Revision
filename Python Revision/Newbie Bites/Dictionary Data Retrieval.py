#Objective: Revise how to retrieve information from a dictionary using the items(), keys() and values() methods

ninjabelt_scores = {'white': 10, 'yellow': 20, 'orange': 30, 'green': 40, 'blue': 50, 'brown': 60, 'black': 70}

#Expected Result: dict_items([('white', 10), ... ('black', 70)])
print(ninjabelt_scores.items())
#Expected Result: dict_keys(['white', ... 'black'])
print(ninjabelt_scores.keys())
#Expected Result: dict_values([10, ... 70])
print(ninjabelt_scores.values())
