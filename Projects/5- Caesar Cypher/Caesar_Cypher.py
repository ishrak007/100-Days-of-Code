
from art_caesarcypher import logo_caesarcypher
alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Defining Functions

def caesar(text_str, shift_no):

    text_list = []
    for i in text_str:
        text_list += i
    final_list = []
    final_msg = ""

    for i in text_list:
        if i in alphabet_lower:
            pointer = alphabet_lower.index(i)
            if direction == '0':
                pointer += shift_no
                pointer %= len(alphabet_lower)
                final_msg = "encode"
            elif direction == '1':
                pointer -= shift_no
                pointer %= len(alphabet_lower)
                final_msg = "decode"
            i = alphabet_lower[pointer]
            final_list += i
        elif i in alphabet_upper:
            pointer = alphabet_upper.index(i)
            if direction == '0':
                pointer += shift_no
                pointer %= len(alphabet_lower)
                final_msg = "encode"
            elif direction == '1':
                pointer -= shift_no
                pointer %= len(alphabet_lower)
                final_msg = "decode"
            i = alphabet_upper[pointer]
            final_list += i
        else:
            final_list += i
    print(f"Your message is: {text_str}")
    print(f"The {final_msg}d message is: {''.join(final_list)}")

# Initialization
print(logo_caesarcypher)
print("Welcome to Caesar Cyper, your personal message Encoder!!")

end_caesar = False
while end_caesar == False:
    direction = input("Type '0' to encrypt, type '1' to decrypt:\n")
    if direction == '0' or direction == '1':
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift)
        repeat = input("Type 'y' if you want to go again. Otherwise type 'n'. ")
        if repeat == 'y':
            continue
        elif repeat == 'n':
            print("Ending Caesar...\nGoodbye :)")
            end_caesar = True
        else:
            print(f"Wrong Key. Try again.")
            continue
    else:
        print(f"Wrong Key. Try again.")
        continue