import random
from dare import dare
from sit import sit
from truth import truth
from random import randint, choice

Game_mode = True
print("hello welcome to the game")
participant = input("How many players are playing, Separated by a comma\n")
no = len(participant)
players = participant.split(",")
while Game_mode:
    target = random.choice(players)
    choice = input(f"{target} choose T or D or S \n")

    if choice == "T":
        truth()
    if choice == "D":
        dare()
    if choice == "S":
        sit()

    route = input("do you want to continue? Y/N? \n")
    if route == "Y":
        Game_mode = True
    else:
        break