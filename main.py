import time
from random import choice

Comp_tally = 0
User_tally = 0
Rock12 = ["rock", "paper", "scissors"]

#1scissors 2paper 3rock

while Comp_tally or User_tally <5:
    User_input = (input("""Rock, Paper or Scissors 
>""")).lower()

    
    Comp_choice = choice(Rock12)

    if User_input != Rock12:
        print("that is not a valid input")
        Response = 0

    if User_input == Comp_choice:
        print("its a draw")
        print(f"you both drew {User_input}")


    if User_input != Comp_choice:
      Loser = (print(f"You Lose!, computer chose {Comp_choice}"))
      if User_input == Rock12[0]  and Comp_choice == Rock12[1] :
        print(Loser)
      elif User_input == Rock12[1] and Comp_choice == Rock12[2] :
        print(Loser)
      elif User_input == Rock12[2] and Comp_choice == Rock12[0] :
        print(Loser)
    
      Comp_tally += 1
    
    else : 
      print(f"You Win!, the computer chose{Comp_choice}")
      User_tally += 1
       
    
  
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