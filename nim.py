import random
import time

pos = 12 #no. of coins left

start = input("Start? (y/n)")
if start == "y":
    first = input("Who goes first? Player or computer? (p/c)")
    if first == "p": #player goes first
        while pos > 0:
            time.sleep(0.5)
            subtract = int(input("How many would you like to take away?")) #subtract is the amount you want to subtract from pos
            if subtract > 3: #if you took more then 3
                print("Uh oh! You took to many!")
                exit("Overdraw")
            pos = pos-subtract
            if pos < 0: #if pos is a negitve num
                print("Uh oh! You took to many!")
                exit("Overdraw")
            subtract = 0
            print("The amount left is", pos, "!")
            if pos == 0: #to win you need to take the last coin
                print("You win!")
            elif pos > 3: #normal computer operation
                time.sleep(0.5)
                print("Computers turn!")
                time.sleep(0.5)
                subtract = random.randint(1, 3)
                print("The computer chose", subtract, "!")
                time.sleep(0.5)
                pos = pos-subtract
                print("Now the amount left is", pos, "!")
                print("your turn!")
            else:
                print("The computer chose", pos, "!")
                time.sleep(0.5)
                pos = pos - pos
                print("Aww man!")
                time.sleep(0.2)
                print("The computer won :(")
                print("Ending...")
                time.sleep(0.5)
                input("Enter to close")
    elif first == "c": #if computer goes first
        print("Computer is making a decision...")
        time.sleep(0.5)
        pos = 12
        while pos > 0:
            if pos > 3: #same code as before I think
                subtract = random.randint(1, 3)
                print("The computer chose", subtract, "!")
                pos = pos-subtract
                time.sleep(0.2)
                print("Now there are", pos, "pieces!")
                subtract = 0
                time.sleep(0.5)
            print("Now it your turn")
            subtract = int(input("How many do you want to take?"))
            if subtract > 3:
                print("Uh oh! You took to many!")
                exit("Overdraw")
            if pos < 0:
                print("Uh oh! You took to many!")
                exit("Overdraw")
            pos = pos - subtract
            if pos == 0:
                print("You won!")
                exit("WIN!")
	print(ending...)
	time.sleep(0.5)
