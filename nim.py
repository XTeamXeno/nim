import random
import time

total = 12  # Number of total coins left


def players_turn(total):
    print("Now its your turn!")
    time.sleep(0.2)
    take_away = int(input("How many coins would you like to take away?"))  # Number of coins to subtract from the total
    time.sleep(0.2)
    if total < 0:  # Invalid
        print("You took to many!")
        exit()
    if take_away > 3:
        print("You took to many!")
        exit()
    print("Ok!")
    time.sleep(0.2)
    total = total - take_away
