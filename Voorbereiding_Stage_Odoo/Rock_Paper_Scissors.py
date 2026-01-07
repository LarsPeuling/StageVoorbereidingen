#Winning Rules as follows:
#Rock vs paper-> paper wins
#Rock vs scissor-> Rock wins
#paper vs scissor-> scissor wins.

import random

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    
    actions ={"rock","paper,""scissors"}
    computer_action = random.choice(list(actions))
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    
    if user_action == computer_action:
        print("draw")
        result = "draw"
    elif (user_action == "rock" and computer_action == "scissors") or (computer_action == "rock"and user_action == "scissors"):
        print("rock wins")
        result = "rock"
    elif (user_action == "paper" and computer_action == "rock") or (computer_action == "paper" and user_action == "rock"):
        print("paper wins")
        result = "paper"
    elif (user_action == "scissors" and computer_action == "paper") or (computer_action == "scissors" and user_action == "paper"):
        print("scissors wins")
        result = "scissors"
    
    if result == "draw":
        print("It's a tie!")
    elif result == user_action:
        print("You win!")
    else:
        print("Computer wins!")
        
    print("Do you want to play again? (yes/no)")
    
    answer = input().lower()
    if answer != "yes":
        break

print("Please play again later!")