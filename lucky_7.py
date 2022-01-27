#####################################################################################
#
# Name:   Ishai Masada
#
# Date:      1/25/22
#
# Purpose:  Show the user's probability disadvantage of Lucky Sevens
#
# Functions:       List of functions being called.
# Update:           If there updates made to the code, add the date and the update.
#
#####################################################################################

import random

players = {}

for player in range(1, 5):

    total_funds = 0
    print("""Welcome to Lucky Sevens!
          If the dice add up to 7, you gain $4.
          If they don\'t, then you lose $1.
          """)
    player_name = input("Type in your name, you fool: ")
    pot = int(input("Type in the amount of money you are willing to put in the pot: "))

    number_of_rolls = 0

    while pot > 0:
        die_1 = random.randint(1, 7)
        die_2 = random.randint(1, 7)

        if die_1 + die_2 == 7:
            pot += 4
        else:
            pot -= 1

        if total_funds < pot:
            total_funds = pot
        number_of_rolls += 1

    players[player_name] = number_of_rolls
    print(f"This is the highest value of the pot in the game: {total_funds}")
    print(f"This is the number of rolls it took the pot to empty: {number_of_rolls}")

print(players)
# Display the name of the player with the largest amount of rolls
print(f"""The player that had the largest amount of
      rolls: {players.keys()[players.values().index(max(players.values()))]}""")

# Display the name of the player with the least amount of rolls
print(f"""The player that had the least amount of
      rolls: {players.keys()[players.values().index(min(players.values()))]}""")
