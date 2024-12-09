import pandas

data = pandas.read_csv(r"./Projects/26- NATO Alphabet/NATO-alphabet-start/nato_phonetic_alphabet.csv")
df = pandas.DataFrame(data)
# print(df)

# natodict = {}
# for (index, row) in df.iterrows():
#     if row.letter == "I":
#         print(row.code)
    
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(nato_dict)

user_input = input("Enter a word: ").upper()

codewords = [nato_dict[letter] for letter in user_input]
print(codewords)

