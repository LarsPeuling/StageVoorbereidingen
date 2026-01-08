#Two players play the game against each other; let's assume Player 1 and Player 2.
# Player 1 plays first by setting a multi-digit number.
# Player 2 now tries his first attempt at guessing the number.
# If Player 2 succeeds in his first attempt (despite odds which are highly unlikely) he wins the game and is crowned Mastermind! 
# If not, then Player 1 hints by revealing which digits or numbers Player 2 got correct.
# The game continues till Player 2 eventually is able to guess the number entirely.
# Now, Player 2 gets to set the number and Player 1 plays the part of guessing the number.
# If Player 1 is able to guess the number within a lesser number of tries than Player 2 took, then Player 1 wins the game and is crowned Mastermind.
# If not, then Player 2 wins the game.

import random

number = random.randrange(0, 1000)
number = str(number).zfill(4)   # ensure 4 digits

number_guess = input("p2, guess the number: ").zfill(4)

if number_guess == number:
    print("Unbelievable, you are now the mastermind!")
else:
    guess_counter = 0

    while number_guess != number:
        guess_counter += 1
        ctr = 0
        correct = ['X'] * 4

        for i in range(4):
            if number_guess[i] == number[i]:
                correct[i] = number_guess[i]
                ctr += 1

        if ctr == 0:
            print("None of the numbers in your input match.")
        else:
            print(f"Not quite, you got {ctr} digit(s) correct: {correct}")

        print()
        number_guess = input("Enter your next choice of numbers: ").zfill(4)

    print(
        f"Congratulations! You guessed the number {number} "
        f"correctly in {guess_counter} attempts and are now the Mastermind!"
    )
