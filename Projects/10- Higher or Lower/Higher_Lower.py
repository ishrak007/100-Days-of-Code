import random
import time
from Higher_Lower_Stuffs import *
from replit import clear

def check_result(ans_str, count_a, count_b):
    correct_ans = ""
    max_one = max(count_a, count_b)
    if max_one == count_a:
        correct_ans = "A"
    else:
        correct_ans = "B"
    if ans_str != "A" and ans_str != "B":
        print("Invalid Key. Type Again.")
        answer = (input("Type 'A' or 'B': ")).upper()
        check_result(answer, count_a, count_b)
    elif ans_str == correct_ans:
        print("right")
        return 0
    elif ans_str != correct_ans:
        print("wrong")
        return 1

def play_game(entry_1, score_count): 

    entry2 = random.choice(data)
    count1 = entry_1['follower_count']
    count2 = entry2['follower_count']
    carry = data.pop(data.index(entry2))  # entry2 is popped now into the carry which will be made entry 1 in the next round
    data.append(entry_1)  # adding back the previously popped entry1 so that the list does not deplete

    msg_a = print(f"Compare A: {entry_1['name']}, a {entry_1['description']} from {entry_1['country']}")
    # print(count1)  # to cheat
    print(logo_vs)
    msg_b = print(f"Against B: {entry2['name']}, a {entry2['description']} from {entry2['country']}")
    # print(count2)
    print("Who has more followers?")

    answer = (input("Type 'A' or 'B': ")).upper()
    result = check_result(answer, count1, count2)

    # Correct Answer. loop going 
    if result == 0:
        clear()
        print(logo_game)
        score_count += 1
        print(f"You're right! Current score: {score_count}.")
        play_game(carry, score_count)
    # Incorrect Answer. Game End
    else:
        clear()
        print(logo_game)
        print(f"Sorry, that's wrong. Final score: {score_count}")

# Starting Game
score = 0
entry1 = random.choice(data)
carry = data.pop(data.index(entry1))  # popping entry1 into variable carry to avoid comparing same entries
print(logo_game)
play_game(carry, score)