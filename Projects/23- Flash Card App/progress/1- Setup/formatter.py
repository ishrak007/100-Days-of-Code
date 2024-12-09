import arabic_reshaper
from bidi.algorithm import get_display

word_str = ""
with open(r"Projects\23- Flash Card App\ar_words_500.txt", "r", encoding="utf-8") as file:
    data = file.readlines()
    for line in data:
        word = (line.strip()).split(" ")[0]
        reshaped_word = arabic_reshaper.reshape(word)
        final_word = get_display(reshaped_word)
        word_str += f"{final_word}\n"
    
with open(r"Projects\23- Flash Card App\arabic_words.txt", "w", encoding="utf-8") as file:
    file.write(get_display(word_str))