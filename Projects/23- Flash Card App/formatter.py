# from bidi.algorithm import get_display
from response_retrievers import *
import csv

# word_str = ""
# with open(r"Projects\23- Flash Card App\spanish data\es_50k.txt", "r", encoding="utf-8") as file:
#     data = file.readlines()
#     for line in data:
#         word = (line.strip()).split(" ")[0]
#         word_str += f"{word}\n"
#         if data.index(line) > 101:
#             break
    
# with open(r"Projects\23- Flash Card App\spanish data\es_100.txt", "w", encoding="utf-8") as file:
#     file.write(word_str)

global word_data
word_data = []
with open(r"Projects\23- Flash Card App\spanish data\es_100.txt", "r", encoding="utf-8") as file:
    data = file.readlines()
    for line in data:
        word_dict = {}
        word = line.strip()
        try:
            translation = get_translation(word, source_lang="es", target_lang="en")
            transliteration = get_transliteration(word)
            example_sentence, sentence_translation = get_spanish_sentence_and_translation(word)
        except:
            continue
        else:
            word_dict["Word"] = word
            word_dict["Translation"] = translation
            word_dict["Transliteration"] = transliteration
            word_dict["Example Sentence"] = example_sentence
            word_dict["Sentence Translation"] = sentence_translation
            print(word_dict)
            word_data.append(word_dict)

# Writing to a CSV file
with open(r'Projects\23- Flash Card App\spanish data\es_word_data.csv', 'w', newline='', encoding="utf-8") as file:
    fieldnames = ["Word", "Translation", "Transliteration", "Example Sentence", "Sentence Translation"]  # Define the order of columns
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Writing the header (column names)
    writer.writeheader()
    
    # Writing the data row by row
    writer.writerows(word_data)
