print("Welcome to Treasure Island!!\nYour mission is to find the treasure")
print("You are at a crossroad. Where do you want to go? Type \"left\" or \"right\"")

direction0 = input("\"left\" or \"right\"")
print(f"Turning {direction0}...")
if direction0 == "right":
    print("You fell into a hole.\nGame Over.\n :(")
elif direction0 == "left":
    print("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
    direction1 = input("\"swim\" or \"wait\"")
    print(direction1 + "ing...")
    if direction1 == "swim":
        print("You got attacked by an angry trout.\nGame Over.\n :(")
    elif direction1 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ")
        direction2 = input("\"red\" or \"blue\" or \"yellow\"")
        print(f"Opening {direction2} door...")
        if direction2 == "red":
            print("Its a room full of fire.\nGame Over.\n :(")
        elif direction2 == "blue":
            print("You enter a room full of beasts.\nGame Over.\n :(")
        elif direction2 == "yellow":
            print("You found the treasure.\nYOU WIN!!\n :)")
        else:
            print("Invalid Key. Game Over\n :'(")
    else:
        print("Invalid Key. Game Over\n :'(")
else:
    print("Invalid Key. Game Over\n :'(")