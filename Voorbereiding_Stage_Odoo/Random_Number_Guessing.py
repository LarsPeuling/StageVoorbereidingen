#scope:
#The objective of this project is to build a simple number guessing game that challenges the user to identify a randomly selected number within a specified range. 
#The game begins by allowing the user to define a range by entering a lower and an upper bound (for example, from A to B). 
#Once the range is set, the system randomly selects an integer that falls within this user-defined interval. 
#The user's task is then to guess the chosen number using as few attempts as possible. 
#The game provides feedback after each guess, helping the user refine their next guess based on whether their previous attempt was too high or too low.

#counter for attempts

import random

x = int(input("Enter the number of attempts you would like to have: "))
print(f"Welcome to the Number Guessing Game! You have {x} attempts to guess the correct number. ")

low = int(input("Enter the lower bound of the range: "))
high = int(input("Enter the upper bound of the range: "))


number_to_guess = random.randint(low, high)
attempt_counter = 0

while attempt_counter < x:
    attempt_counter += 1
    attempt = int(input("enter your guess: "))
    
    if attempt == number_to_guess:
        print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempt_counter} attempts.")
        break
    elif attempt < number_to_guess:
        print("Your guess is too low. Try again.")
    elif attempt > number_to_guess:
        print("your guess is to high. try again.")
    elif attempt_counter >= x:
        print(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}.")
    