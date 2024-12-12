
# INITIALIZATION
import random
from Hangman_Arts import *
from Word_Catalogue import *

# INITIAL DISPLAY
print(logo_welcome[0])
print(logo_hangman[0])
print("Guess the correct word. Save the innocent man!!")
print(''' 
            +---+
                |
                |
    O           |
   /|\          |
    |           |
   / \    ===========               
    
      ''')

# GENERATING WORDS
chosen_word = random.choice(word_catalog)
chosen_list = []
for i in chosen_word:
    chosen_list += i
lives = 6

# TESTING CODE
# Print out if you don't want to cheat
print(f'The solution is {chosen_word}.')

# BLANK GENERATION
blank_OG = "_"
word_len = len(chosen_word)
blank_list = []
for i in range(word_len):
    blank_list += blank_OG
print(f"{' '.join(blank_list)}\n")

# SETTING CONDITIONS

game_ends = False

while game_ends == False:
    if blank_list == chosen_list:
        game_ends = True
        print("You Win!!")
    elif lives == 0:
        game_ends = True
        print(f"\n\nCorrect Word is \"{chosen_word.upper()}\".\n")
        print("You Lose.\n :'(")
    else:
        guess = input("Guess a letter: ")
        if guess in blank_list:
            print("Letter already guessed.")
        else: 
            if guess in chosen_list:
                for i in range(word_len):
                    if chosen_list[i] == guess:
                        blank_list[i] = guess
            else:
                lives -= 1
                print(f"'{guess}' is not in the word. Wrong Guess.")
                print(f"{stages[lives]}")
            print(f"{' '.join(blank_list)}")
            print(f"Chances Remaining: {lives}")
