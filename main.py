import time
from random import choice

Comp_tally = 0
User_tally = 0
Rock12 = ["rock", "paper", "scissors"]

#1scissors 2paper 3rock

while Comp_tally or User_tally <5:
    User_input = (input("""Rock, Paper or Scissors 
>""")).lower()

    Comp_choice = choice([1,2,3])

    if User_input == Rock12[0]:
        Response = 3
    elif User_input == Rock12[1]:
        Response = 2
    elif User_input == Rock12[2]:
        Response = 1
    elif User_input != Rock12:
        print("that is not a valid input")
        Response = 0

    if Response == Comp_choice:
        print("its a draw")
        print(f"you both drew {User_input}")

    if Response != Comp_choice:
        if Response == 1 and Comp_choice == 2 :
            print("You Win, the computer chose Paper")
            User_tally += 1
        if Response == 2 and Comp_choice == 3 :
            print("You win, the computer chose Rock")
            User_tally += 1
        if Response == 3 and Comp_choice == 1 :
            print("You win, the computer chose Scissors")
            User_tally += 1
        if Response == 1 and Comp_choice == 3 :
            print("You lose, the computer chose Rock")
            Comp_tally += 1
        if Response == 2 and Comp_choice == 1 :
            print("You lose, the computer chose Scissors")
            Comp_tally += 1
        if Response == 3 and Comp_choice == 2 :
            print("You lose, the computer chose Paper")
            Comp_tally += 1
    print(f"""    SCORE
Computer:{Comp_tally}
Player:{User_tally}""")
    if Response == 0:
        print("Try again")
    if Comp_tally == 5:
        print("YOU WERE BEATEN BY THE COMPUTER")
        break
    if User_tally == 5:
        print("YOU BEAT THE COMPUTER")
        break
    time.sleep(5)

print("Game over!!")