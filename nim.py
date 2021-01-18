import random
import time

coins_left = 12  # Number of total coins left


def players_turn(total):  # define players choices and total will equal coins_left later in the code
    print("Now its your turn!")
    time.sleep(0.2)
    take_away = int(input("How many coins would you like to take away? (1/2/3)"))
    # Number of coins to subtract from the total
    time.sleep(0.2)
    if total < 0:  # Too many
        print("You took to many!")
        exit()
    if take_away > 3:  # Too many
        print("You took to many!")
        exit()
    if take_away < 1:  # Too few
        print("You took to few")
        exit()
    print("Ok!")
    time.sleep(0.2)
    total = total - take_away
    return total  # return amount left as total


def computers_turn(total):  # define computers action
    print("Now its the computers turn!")
    time.sleep(0.2)
    subtract = 0
    if total > 3:
        subtract = random.randint(1, 3)  # randomly choose
    if total <= 3:
        subtract = total  # win if possible
    total = total-subtract
    return total  # return amount left as total


start = input("Do you want to play nim? (y/n)")  # ask if they want to play
if start == "y":
    print("Ok!")
    time.sleep(0.2)
    while coins_left > 0:
        coins_left = players_turn(coins_left)  # do players turn
        print("There are now", coins_left, "amount of coins left!")
        if coins_left == 0:  # win for player
            print("Congrats! You win!")
            time.sleep(0.5)
            exit("win")
        coins_left = computers_turn(coins_left)
        print("There are now", coins_left, "amount of coins left!")
        if coins_left == 0:  # win for computer
            print("Aww man! The computer won!")
            time.sleep(0.5)
            exit("lose")
elif start == "n":
    print("Ok!")
    time.sleep(0.5)
    exit("responded n to start")
else:
    print("Invalid answer!")
    time.sleep(0.5)
    exit("invalid response to start")
