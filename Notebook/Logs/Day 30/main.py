
def take_user_input():
    global word
    word = input("Enter a word: ").upper()
    try:
        if not word.isalpha():
            raise KeyError
    except:
        print("Sorry, only letters in the alphabet please.")
        take_user_input()
    finally:
        return word

import pandas

data = pandas.read_csv(r"Notebook\##files\Day 30\nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = take_user_input()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
