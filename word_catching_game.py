import time
import random 
from hangman.words import words 
import os



word = random.choice(words).lower()
word_letters = ""
for number in range(0,len(word)):
    word_letters += word[number]
    for letter in word_letters:
        print(letter)
    time.sleep(1.3)
    os.system("cls")
    guess = input("Repeat: ")
    if guess != word_letters:
        break
 
if word_letters == word:
    print(f"Congratulations, You find the '{word_letters}'")
else:
    print("Game Over!! You can try again ")



