# ---------------------------- IMPORTS ------------------------------- #
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
from response_retrievers import *
import pandas, csv, os

# ---------------------------- CONSTANTS ------------------------------- #
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 450
FONT_ARABIC = ("Ariel", 40, "normal")
FONT_ENGLISH = ("Ariel", 60, "bold")
BLUE = "#99cede"
GRAY = "#bbbebf"
LIGHT_GRAY = "#d5dcde"
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color = BACKGROUND_COLOR)
        
        # window setup
        self._set_appearance_mode("light")
        self.iconbitmap(r"Projects\23- Flash Card App\images\empty.ico")
        self.title('Flash Pal')
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.configure(pady=25)
        self.resizable(False, False)
        self.init_essentials()
        self.place_widgets()
        self.generate_card("")
        
        # events
        self.bind("<Escape>", lambda event: self.destroy())

        # run
        self.mainloop()
        
    def init_essentials(self):
        
        # images
        img_tick = Image.open(r"Projects\23- Flash Card App\images\right.png")
        self.tick_image = ctk.CTkImage(light_image=img_tick, dark_image=img_tick, size=(70, 70))
        
        img_cross = Image.open(r"Projects\23- Flash Card App\images\wrong.png")
        self.cross_image = ctk.CTkImage(light_image=img_cross, dark_image=img_cross, size=(70, 70))
        
        card_back_img = Image.open(r"Projects\23- Flash Card App\images\card_back.png").resize((1200,800))
        self.card_back = ImageTk.PhotoImage(image=card_back_img)
        
        card_front_img = Image.open(r"Projects\23- Flash Card App\images\card_front.png").resize((1200,800))
        self.card_front = ImageTk.PhotoImage(image=card_front_img)
        
        # word data
        try:
            with open(r'Projects\23- Flash Card App\spanish data\words_to_learn.csv', 'r', encoding="utf-8") as file:
                df = pandas.read_csv(file)
        except:
            with open(r'Projects\23- Flash Card App\spanish data/sample.csv', 'r', encoding="utf-8") as file:
                df = pandas.read_csv(file)
        finally:
                self.word_data = df.to_dict(orient="records")
            
        # vars
        self.word = tk.StringVar()
        self.translation = tk.StringVar()
        self.transliteration = tk.StringVar()
        self.example_sentence = tk.StringVar()
        self.sentence_translation = tk.StringVar()
        self.flip_timer = None
        
    def place_widgets(self):
        
        # layout
        self.rowconfigure(0, weight=4, uniform="a")
        self.rowconfigure(1, weight=1, uniform="a")
        self.columnconfigure((0,1), weight=1, uniform="a")
        
        # Canvas (Card Front)
        self.canvas = FlashCardFront(self, self.card_front, self.word)
        
        # buttons
        cross = ctk.CTkButton(self,
                              fg_color='transparent',
                              border_width=0,
                              hover=False,
                              text="",
                              width=80,
                              height=80,
                              image=self.cross_image,
                              command=lambda: self.generate_card("cross")
                              )
        cross.grid(row=1, column=0, sticky="n")
        
        tick = ctk.CTkButton(self,
                             fg_color='transparent',
                             border_width=0,
                             hover=False,
                             text="",
                             width=80,
                             height=80,
                             image=self.tick_image,
                             command=lambda: self.generate_card("tick")
                             )
        tick.grid(row=1, column=1, sticky="n")

    def generate_card_data(self):
        
        word_dict = random.choice(self.word_data)
        self.word = word_dict["Word"]
        self.translation = word_dict["Translation"]
        self.transliteration = word_dict["Transliteration"]
        self.example_sentence = word_dict["Example Sentence"]
        self.sentence_translation = word_dict["Sentence Translation"]
        
        return word_dict
        
    def generate_card(self, action):
        
        if self.flip_timer:
            self.after_cancel(self.flip_timer)
        cur_word_dict = self.generate_card_data()
        self.canvas = FlashCardFront(self, self.card_front, self.word)
        self.canvas.itemconfig(self.canvas.word, text=self.word)
        self.flip_timer = self.after(3000, self.flip_card)
        
        if action == "tick":
            
            # removing the current word from words to learn
            self.word_data.remove(cur_word_dict)
            
            # Writing to a new CSV file
            with open(r'Projects/23- Flash Card App/spanish data\words_to_learn.csv', 'w', newline='', encoding="utf-8") as file:
                fieldnames = ["Word", "Translation", "Transliteration", "Example Sentence", "Sentence Translation"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                # Writing the header (column names)
                writer.writeheader()
                
                # Writing the data row by row
                writer.writerows(self.word_data)    
                    
            if len(self.word_data) < 1:
                # Example of deleting a file
                file_path = r"Projects\23- Flash Card App\spanish data\words_to_learn.csv"
                try:
                    os.remove(file_path)
                    print(f"{file_path} has been deleted successfully.")
                except FileNotFoundError:
                    print(f"{file_path} does not exist.")
                except Exception as e:
                    print(f"Error occurred while deleting the file: {e}")
        
    def flip_card(self):
        
        self.canvas = FlashCardBack(self, 
                                    bg_image=self.card_back, 
                                    word=self.word, 
                                    translation=self.translation, 
                                    transliteration=self.transliteration,
                                    example_sentence=self.example_sentence,
                                    sentence_translation=self.sentence_translation
                                    )     

class FlashCard(tk.Canvas):
    def __init__(self, master):
        super().__init__(master=master, 
                         highlightthickness=0,
                         background=BACKGROUND_COLOR,
                         width=1200,
                         height=800,
                         )
        self.grid(row=0, column=0, columnspan=2, sticky="s")
        
class FlashCardBack(FlashCard):
    def __init__(self, master, bg_image, word, translation, transliteration, example_sentence, sentence_translation):
        super().__init__(master=master)
        self.create_image(600, 400, image=bg_image)
        self.create_text(600, 250, text=word, font=("Ariel", 50, "normal"), fill="white")
        self.create_text(600, 400, text=translation, font=("Ariel", 70, "bold"), fill="white")
        self.create_text(600, 500, text=transliteration, font=("Ariel", 35, "italic"), fill="white")
        self.create_text(600, 640, text=example_sentence, font=("Ariel", 30, "normal"), fill="white")
        self.create_text(600, 690, text=sentence_translation, font=("Ariel", 30, "normal"), fill="white")
        
class FlashCardFront(FlashCard):
    def __init__(self, master, bg_image, word):
        super().__init__(master=master)
        self.create_image(600, 400, image=bg_image)
        self.create_text(600, 250, text="Spanish", font=("Ariel", 50, "italic"))
        self.word = self.create_text(600, 450, text=word, font=("Ariel", 70, "bold"))
        
if __name__ == '__main__':
    app = App()
