import random
import time
import os
sleep2 = time.sleep(0.2)
sleep5 = time.sleep(0.5)   # For testing where I went wrong
coins_left = 12  # Number of total coins left
active = True  # Start loop active
while active:
    start = input("Do you want to play nim? (y/n)")
    if start == "y":
        print("OK! Starting game.")
        sleep2
        active = False
    elif start == "n":
        print("OK! Ending program.")
        input("(Press enter to exit)")
        exit()
    else:
        print("You entered an incorrect string! Try again please!")
sleep5
os.system("cls")
active = True  # Game loop active
while active:
    # Player turn
    print("Its your turn!")
    sleep2
    print("There are",coins_left,"coins left.")
    sleep2
    take_away_active = True
    while take_away_active:
        try_loop_active = True
        while try_loop_active:
            try:
                coins_to_take_away = int(input("How many coins would you like to take away? (1 though 3)"))
                try_loop_active = False
            except Exception:
                print("Woops! That is not an int! Try again.")
        try:
            if coins_to_take_away > 3:
                print("Woops! Thats too many! Try again.")
            elif coins_to_take_away < 1:
                print("Woops! Thats too few! Try again.")
            else:
                coins_left = coins_left - coins_to_take_away
                print("Now there are", coins_left, "coins left!")
                sleep5
        except Exception:
            print("Woops! Thats not a int! Try again.")
        sleep5
        # "AI" Turn
        os.system("cls")
        print("Now its the ai's turn!")
        sleep2
        coins_to_take_away = random.randint(1,3)
        print("The ai choose", coins_to_take_away, "coins to take away!")
        sleep2
        print("Now there are", coins_left, "coins left!")
        # TODO: add win condishions and fix spelling