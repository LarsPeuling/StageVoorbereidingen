#The Hangman program randomly selects a secret word from a list of secret words. The random module will provide this ability, so line 1 in program imports it.
#   The Game: Here, a random word (a fruit name) is picked up from our collection and the player gets limited chances to win the game.
#   When a letter in that word is guessed correctly, that letter position in the word is made visible. 
#   In this way, all letters of the word are to be guessed before all the chances are over. 
#   For convenience, we have given length of word + 2 chances. For example, word to be guessed is mango, then user gets 5 + 2 = 7 chances, as mango is a five-letter word.

import random
from collections import Counter

secret_words = ['apple', 'banana', 'orange', 'grape', 'mango', 'peach', 'cherry', 'pear', 'plum', 'kiwi']

word = random.choice(secret_words)

print("\nWelcome to Hangman! Guess the word before your chases are over. Hint: It's a fruit.")

for i in word:
    print("_", end=" ")
print()

playing = True
chances = len(word) + 2
letter_guessed = ""
correct = 0
flag = 0

while (chances != 0) and flag == 0:
    print()
    chances -= 1
    
    try:
        guess = input("Enter only a single letter: ")
    except:
        print("Enter only a letter")
        continue
    
    if not guess.isalpha():
        print("Enter only a letter")
        continue
    elif len(guess) > 1:
        print("Enter only a single letter")
        continue
    elif guess in letter_guessed:
        print("You have already guessed that letter. Try a different letter.")
        continue
    
    if guess in word:
        k = word.count(guess)
        for _ in range(k):
            letter_guessed += guess
            
    for char in word:
        if char in letter_guessed and (Counter(letter_guessed) != Counter(word)):
            print(char, end=" ")
            correct += 1
            
        elif (Counter(letter_guessed) == Counter(word)):
            print("the word is: ", end="")
            print(word)
            flag = 1
            print("Congratulations! You guessed the word correctly.")
            break
            break
        else:
            print("_", end=" ")
if chances <= 0 and (Counter(letter_guessed) != Counter(word)):
    print("\nSorry, you have run out of chances. The word was:", word)
    
    