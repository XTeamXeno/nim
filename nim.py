import random
import time
import os
coins_left = 12  # Number of total coins left
active = True  # Start loop active
while active:
    start = input("Do you want to play nim? (y/n)")
    if start == "y":
        print("OK! Starting game.")
        time.sleep(0.2)
        active = False
    elif start == "n":
        print("OK! Ending program.")
        input("(Press enter to end)")
        exit()
    else:
        print("You entered an incorrect string! Try again please!")
time.sleep(0.5)
os.system("cls")
active = True  # Game loop active
while active:
    # Player turn
    print("Its your turn!")
    time.sleep(0.2)
    take_away_active = True
    while take_away_active:
        try_loop_active = True
        while try_loop_active:
            try:
                print("There are",coins_left,"coins left.")
                time.sleep(0.2)
                coins_to_take_away = int(input("How many coins would you like to take away? (1 though 3)"))
                try_loop_active = False
            except Exception:
                print("Woops! That is not an int! Try again.")
            try:
                if coins_to_take_away > 3:
                    print("Woops! Thats too many! Try again.")
                elif coins_to_take_away < 1:
                    print("Woops! Thats too few! Try again.")
            except Exception:
                print("Woops! Thats not a int! Try again.")
            if coins_to_take_away > coins_left:
                print("Thats too many! The computer won! Better luck next time")
                input("Enter to end")
                exit()
            else:
                coins_left = coins_left - coins_to_take_away
                print("Now there are", coins_left, "coins left!")
                time.sleep(0.5)
        if coins_left >= 1:
            pass
        elif coins_left < 1:
            print("The computer lost! Congrats!")
        time.sleep(0.2)
        # "AI" Turn
        os.system("cls")
        print("Now its the ai's turn!")
        time.sleep(0.2)
        coins_to_take_away = random.randint(1,3)
        if coins_left > 0:
            print("The ai choose", coins_to_take_away, "coins to take away!")
            coins_left = coins_left - coins_to_take_away
        elif coins_left < 0:
            print("The computer lost! Congrats!")
            input("Enter to end")
            exit()
        elif coins_left == 0:
            print("The computer won! Better luck next time")
            input("Enter to end")
        time.sleep(0.2)