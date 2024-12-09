import random
from replit import clear
from Blackjack_Stuff import *
import time
    
player_cards = []
computer_cards = []

# Adding Cards
def add_card(cards_list):
    card_choice = random.choice(list(deck.keys()))
    cards_list.append(card_choice)
    return cards_list

# Checking Values
def value_checker(cards_list):
    cur_score = 0
    for i in cards_list:
        cur_score += deck[i]
    n = cards_list.count('A')
    if n > 1:
        cur_score -= 10 * (n-1)    # Ace will only be counted once as 11 and thereupon as 1
    return cur_score

# Display Stats
def display_stats(player_cards_list, comp_cards_list):
    print(f"Your final hand: {player_cards_list}, Final Score: {value_checker(player_cards_list)}")
    print(f"Computer's final hand: {comp_cards_list}, Final Score: {value_checker(comp_cards_list)}")

# Closing up on 21
def find_closest(play_val, comp_val):
    diff_p = abs(21 - play_val)
    diff_c = abs(21 - comp_val)
    if diff_p > diff_c:
        return "You lose :'("
    else:
        return "YOU WIN!! :')"    
    
# Checking for blackjack (an 'A' and a '10' on 1st 2 cards)
def check_blackjack(card_list):
    if 'A' in card_list:
        if '10' in card_list:
            return True

# Checking for Winner 
def check_win_terminal(play_val, comp_val):
    if play_val == comp_val:
        print("Its a Tie!!")
    elif play_val > 21:
        print("You went over.\nYou lose :'(")
    elif comp_val > 21:
        print(f"Opponent went over.\nYOU WIN!! :')")
    else:
        print(find_closest(play_val, comp_val))

# Setting the loop
def loop_or_not(add_statement, player_cards_list, comp_cards_list):
    
    final_comp_val = value_checker(comp_cards_list)
    if add_statement == 'y':
        add_card(player_cards_list) 
        current_player_val = value_checker(player_cards_list)  
        if final_comp_val == current_player_val:  
            display_stats(player_cards_list, comp_cards_list)
            print(f"Its a Tie!!")
        elif current_player_val > 21 and final_comp_val > 21:
            display_stats(player_cards_list, comp_cards_list)
            print("Both went over.\nNo Wins :'(")
        elif current_player_val > 21:
            display_stats(player_cards_list, comp_cards_list)
            print("You went over.\nYou lose :'(")
        elif final_comp_val > 21:  
            display_stats(player_cards_list, comp_cards_list)
            print(f"Opponent went over.\nYOU WIN!! :')")
        else:
            print(f"Your cards: {player_cards_list}, Current Score: {current_player_val}")
            print(f"Computer's first card: {comp_cards_list[0]}")
            print("Type 'y' to get another card. Type 'n' to pass. ")
            add_statement = input("'y' or 'n'? ")
            loop_or_not(add_statement, player_cards_list, comp_cards_list)   
    elif add_statement == 'n':
        final_player_val = value_checker(player_cards_list)
        final_comp_val = value_checker(comp_cards_list)
        display_stats(player_cards_list, comp_cards_list)
        check_win_terminal(final_player_val, final_comp_val)
    else:
        print("Invaid key. Try again. ")
        add_statement = input("'y' or 'n'? ")
        loop_or_not(add_statement, player_cards_list, comp_cards_list)
        
# Setting the UI

print(logo)
print("Welcome to The Blackjack Game!!")
print("Do you want to play a round of Blackjack?")
game_start = input("Type 'y' or 'n': ")

game_end = False
while not game_end:
    if game_start == 'n':
        print("Exiting Game...")
        time.sleep(1)
        print("Goodbye")
        game_end = True
    elif game_start == 'y':
        print("Starting New Game...")
        time.sleep(1)
        add_card(player_cards)
        add_card(player_cards) 
        add_card(computer_cards)
        add_card(computer_cards)
        print(f"Your cards: {player_cards}, Current Score: {value_checker(player_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        print("Type 'y' to get another card. Type 'n' to pass. ")
        statement = input("'y' or 'n'? ")
        bjack1 = check_blackjack(player_cards)
        bjack2 = check_blackjack(computer_cards)
        if bjack1 and bjack2:
            display_stats(player_cards, computer_cards)
            print("You have both found the Blackjack!!\n It's a tie :)")
        elif bjack1:
            display_stats(player_cards, computer_cards)
            print("Congratulations. You have found the Blackjack!!\nYOU WIN!! :')")
        elif bjack2:
            display_stats(player_cards, computer_cards)
            print("Oh No. Opponent has found the Blackjack.\nYou Lose :'(")
        else:
            while value_checker(computer_cards) < 17:
                add_card(computer_cards)
            loop_or_not(statement, player_cards, computer_cards)
        print("Do you want to go for another round of Blackjack? ")
        game_start = input("Type 'y' or 'n': ")
        player_cards.clear()
        computer_cards.clear()
        clear()
    else:
        print("Invaid key. Try again. ")
        game_start = input("Type 'y' or 'n': ")
        continue
