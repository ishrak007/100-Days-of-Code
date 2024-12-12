# ---------------------------- IMPORTS ------------------------------- #
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import arabic_reshaper
from bidi.algorithm import get_display
from response_retrievers import *

# ---------------------------- CONSTANTS ------------------------------- #
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 450
FONT_ARABIC = ("Ariel", 40, "normal")
FONT_ENGLISH = ("Ariel", 60, "bold")
BLUE = "#99cede"
GRAY = "#bbbebf"
LIGHT_GRAY = "#d5dcde"
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- DATA SETUP ------------------------------- #





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
        self.init_vars()
        self.place_widgets()
        
        # events
        self.bind("<Escape>", lambda event: self.destroy())

        # run
        self.mainloop()
        
    def init_vars(self):
        
        img_tick = Image.open(r"Projects\23- Flash Card App\images\right.png")
        self.tick_image = ctk.CTkImage(light_image=img_tick, dark_image=img_tick, size=(70, 70))
        
        img_cross = Image.open(r"Projects\23- Flash Card App\images\wrong.png")
        self.cross_image = ctk.CTkImage(light_image=img_cross, dark_image=img_cross, size=(70, 70))
        
        card_back_img = Image.open(r"Projects\23- Flash Card App\images\card_back.png")
        self.card_back = ImageTk.PhotoImage(image=card_back_img)
        
        card_front_img = Image.open(r"Projects\23- Flash Card App\images\card_front.png").resize((1200,800))
        self.card_front = ImageTk.PhotoImage(image=card_front_img)
        
    def place_widgets(self):
        
        # layout
        self.rowconfigure(0, weight=4, uniform="a")
        self.rowconfigure(1, weight=1, uniform="a")
        self.columnconfigure((0,1), weight=1, uniform="a")

        # canvas
        self.canvas = tk.Canvas(self,
                           highlightthickness=0,
                           background=BACKGROUND_COLOR,
                           width=1200,
                           height=800,
                           )
        self.canvas.grid(row=0, column=0, columnspan=2, sticky="s")
        self.canvas.create_image(600, 400, image=self.card_front)
        self.canvas.create_text(600, 250, text="Arabic", font=("Ariel", 50, "normal"))
        self.canvas.create_text(600, 400, text="English", font=("Ariel", 70, "bold"))
        self.canvas.create_text(600, 500, text="Transliteration", font=("Ariel", 30, "italic"))
        self.canvas.create_text(600, 650, text="Word Meaning", font=("Ariel", 30, "normal"))
        
        # buttons
        cross = ctk.CTkButton(self,
                              fg_color='transparent',
                              border_width=0,
                              hover=False,
                              text="",
                              width=80,
                              height=80,
                              image=self.cross_image,
                              command=lambda: print("cross")
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
                             command=lambda: print("tick")
                             )
        tick.grid(row=1, column=1, sticky="n")





if __name__ == '__main__':
    app = App()
