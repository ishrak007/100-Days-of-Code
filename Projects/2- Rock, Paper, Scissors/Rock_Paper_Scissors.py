import random
print("Welcome to The Rock, Paper & Scissors Game!!")
print("State your choice. Type 'r' for Rock, 'p' for Paper and 's' for scissors.")

user_input = input("What do you choose? ")
if user_input!="r" and user_input!="p" and user_input!="s":
    print("You typed an invalid key. You Lose")
else:
    user_choice = ""
    if user_input == "r":
        user_choice = "ROCK"
        print(f"You chose: {user_choice}")
    elif user_input == "p":
        user_choice = "PAPER"
        print(f"You chose: {user_choice}")
    elif user_input == "s":
        user_choice = "SCISSORS"
        print(f"You chose: {user_choice}")

    choices = ["ROCK", "PAPER", "SCISSORS"]
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("Its a tie!!")
    elif user_choice == "ROCK" and computer_choice == "SCISSORS":
        print("You Win!! :)")
    elif user_choice == "SCISSORS" and computer_choice == "PAPER":
        print("You Win!! :)")
    elif user_choice == "PAPER" and computer_choice == "ROCK":
        print("You Win!! :)")
    else:
        print("You Lose :'(")