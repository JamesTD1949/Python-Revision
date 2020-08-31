#Objective: Revise how to loop through a dictionary and retrieve data from a tuple
games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)


def print_game_stats(games_won):
    """Loop through games_won's dict (key, value) pairs (dict.items)
       printing how many games each person has won,
       pluralize 'game' based on number.
    """
    for item in games_won.items():
        if item[1] != 1:
            print(f"{item[0]} has won {item[1]} games")
        else:
            print(f"{item[0]} has won {item[1]} game")
