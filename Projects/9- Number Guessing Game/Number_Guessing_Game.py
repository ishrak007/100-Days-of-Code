import random
from Number_Guessing_Game_logo import *
import time
from replit import clear

# The Game
def play_game():
    
    print("Starting Game...")
    time.sleep(1)
    
    # Declaring Difficulty
    mode = (input("Choose a difficulty. Type 'easy' or 'hard': ")).upper()
    wrong_key1 = True
    while wrong_key1:
        if mode == "HARD":
            attempts = 5
            wrong_key1 = False
        elif mode == "EASY":
            attempts = 10
            wrong_key1 = False
        else:
            print("Invalid key. Type again.")
            mode = (input("Type 'easy' or 'hard': ")).upper()
    print(f"Difficulty Level: {mode}")
    
    # Generating the Guess
    generated_num = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    print(generated_num)

    # Checking the guesses
    for i in range(attempts):
        generated_num
        attempts -= 1
        guess = int(input("Make a guess: "))
        if guess == generated_num:
            print(f"You Got It!!\nThe correct number is: {generated_num}")
            print("You win!!")
            break
        if guess > generated_num:
            print("Too High.")
        if guess < generated_num:
            print("Too Low.")  
        if attempts > 1: 
            print(f"Guess again.\nYou have {attempts} attempts remaining to guess the number")
        elif attempts == 1:
            print(f"Guess again.\nYou have {attempts} attempt remaining to guess the number")
        else:
            print(f"You've run out of guesses.\nThe correct number is: {generated_num}")
            print("You lose :'(")
            
# The Loop
def loop_game(start_str):
    if start_str == 'y':
        play_game()
        print("Do you want another go?")
        restart_str = input("Type 'y' or 'n': ")
        if restart_str == 'y':
            clear()
            print(logo)
        loop_game(restart_str)
    elif start_str == 'n':
        print("Exiting Game...")
        time.sleep(1)
        print("Goodbye")
    else: 
        print("Invalid key. Type again.")
        retype_str = input("Type 'y' or 'n': ")
        loop_game(retype_str)
        
# UI
print(logo)
print("Welcome to the Number Guessing Game!")
print("Can you guess the correct number?")
print("Lets start a game!!")
start = input("Type 'y' or 'n': ")
loop_game(start)
