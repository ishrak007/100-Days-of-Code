import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!!")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_numbers = int(input("How many numbers would you like? \n"))

# Easy Level

# choice_letters = ""
# for i in range(nr_letters): 
#     choice_letters += random.choice(letters)
# # print(choice_letters)

# choice_symbols = ""
# for i in range(nr_symbols): 
#     choice_symbols += random.choice(symbols)
# # print(choice_symbols)

# choice_numbers = ""
# for i in range(nr_numbers): 
#     choice_numbers += random.choice(numbers)
# # print(choice_numbers)

# chosen_str = choice_letters + choice_symbols + choice_numbers

# print(f"Here is your password: {chosen_str}")

# Hard Level

choice_letters = []
for i in range(nr_letters): 
    choice_letters += random.choice(letters)

choice_symbols = []
for i in range(nr_symbols): 
    choice_symbols.append(random.choice(symbols))

choice_numbers = []
for i in range(nr_numbers): 
    choice_numbers += random.choice(numbers)

chosen_list = choice_letters + choice_symbols + choice_numbers
# print(chosen_list)
random.shuffle(chosen_list)

final_str = ""
for i in chosen_list:
    final_str += i

print(f"Here is your password: {final_str}")