import random
import time
import os

coins_left = 12  # Number of total coins left
active = True
while active:
    start = input("Do you want to play nim? (y/n)")
    if start == "y":
        print("OK! Starting game")
        time.sleep(0.2)
        active = False
    elif start == "n":
        print("OK! Ending program")
        input("(Press enter to exit)")
        exit()
    else:
        print("You entered an incorrect string! Try again please!")
time.sleep(0.5)