#This program is a simple word-guessing game where the user has to guess the characters in a randomly selected word within a limited number of attempts. 
# The program provides feedback after each guess, helping the user to either complete the word or lose the game based on their guesses.

import random
from english_words import get_english_words_set

name = input("Enter your name: ")
print(f"Welcome to the Word Guessing Game, {name}! Good Luck!")

words_List = []

english_words = get_english_words_set(['web2'], lower=True)
word_Lengt = int(input("Enter the number of letters you want to choose from "))
word_counter = 1
while len(words_List) < word_counter:
    word = random.choice(list(english_words))
    if word not in words_List and len(word) >= word_Lengt:
        words_List.append(word)
        
word_to_guess = random.choice(words_List)

#guess the characters
guesses = ''
max_attempts = len(word_to_guess) + 4

while max_attempts > 0:
    failed = 0
    for char in word_to_guess:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
            failed += 1
       
    if failed == 0:
        print(f"\nCongratulations {name}! You've guessed the word '{word_to_guess}' correctly!")
        break
    print()
    guess = input("\nGuess a character: ").lower()
    
    guesses += guess
    
    if guess not in word_to_guess:
        max_attempts -= 1
        print(f"Wrong guess. You have {max_attempts} attempts left.")
        
        if max_attempts == 0:
            print(f"Sorry, you've run out of attempts. The correct word was '{word_to_guess}'.")
            
        
        
        
        
        
        
        
        
        