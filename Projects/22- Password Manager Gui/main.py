# ---------------------------- IMPORTS ------------------------------- #
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
WINDOW_WIDTH, WINDOW_HEIGHT = 525, 350
FONT_LABEL = ("Helvetica", 13, "bold")
FONT_INPUT = ("Helvetica", 13, "normal")
BLUE = "#99cede"
GRAY = "#bbbebf"
LIGHT_GRAY = "#d5dcde"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- UI SETUP ------------------------------- #
class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color = "white")
        
        # window setup
        self._set_appearance_mode("light")
        self.iconbitmap(r"Projects\29- Password Manager Gui\empty.ico")
        self.title('Password Manager')
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False, False)
        self.init_vars()
        self.place_widgets()
        
        # events
        self.bind("<Escape>", lambda event: self.destroy())

        # run
        self.mainloop()
        
    def init_vars(self):
        self.vars_dict = {"Website": tk.StringVar(),
                          "Email/Username": tk.StringVar(),
                          "Password": tk.StringVar()
                          }
        
        # tracing
        for var in list(self.vars_dict.values()):
            var.trace_add("write", self.check_entries)
            
        # text holders
        self.website = ""
        self.email = ""
        self.password = ""
        
        # save dir
        self.save_dir = r"Projects\29- Password Manager Gui\Passes.txt"
        
    def place_widgets(self):
    
        # layout
        self.rowconfigure(0, weight=1, uniform="a")
        self.rowconfigure(1, weight=3, uniform="a")
        self.rowconfigure(2, weight=2, uniform="a")
        self.rowconfigure(3, weight=1, uniform="a")
        self.columnconfigure((0,2), weight=1, uniform="a")
        self.columnconfigure((1), weight=3, uniform="a")
        
        # canvas
        canvas = tk.Canvas(self, 
                           highlightthickness=0,
                           relief="ridge",
                           background="white",
                           )
        canvas.grid(row=1, column=1, sticky="nswe")
        img = Image.open(r"Projects\29- Password Manager Gui\logo.png")
        size = img.size
        self.logo_img = ImageTk.PhotoImage(image=img.resize((size[0]*2, size[1]*2)))
        canvas.create_image(WINDOW_WIDTH * 0.75, WINDOW_HEIGHT * 0.5, image=self.logo_img)
        
        # bottom frame
        bottom = tk.Frame(self, background="white")
        bottom.grid(row=2, column=0, columnspan=5, sticky="nswe", padx=75)
        bottom.rowconfigure((0,1,2,3), weight=1, uniform="b")
        bottom.columnconfigure(0, weight=2, uniform="b")
        bottom.columnconfigure(1, weight=3, uniform="b")
        bottom.columnconfigure(2, weight=2, uniform="b")
        
        # labels
        for info in [("Website:", 0), ("Email/Username:", 1), ("Password:", 2)]:
            label = ctk.CTkLabel(bottom,
                                text_color="black",
                                font=FONT_LABEL,
                                text=info[0],
                                )
            label.grid(row=info[1], column=0)
        
        # entries
        for info in [("Website", 0), ("Email/Username", 1), ("Password", 2)]:
            entry = ctk.CTkEntry(bottom, 
                                text_color="black",
                                font=FONT_INPUT,
                                border_color=GRAY,
                                corner_radius=0,
                                fg_color="white",
                                textvariable=self.vars_dict[info[0]],
                                border_width=1,
                                bg_color=BLUE
                                )
            entry.grid(row=info[1], 
                       column=1, 
                       columnspan=1 if not info[1] == 1 else 2, 
                       sticky="nswe",
                       padx=1,
                       pady=1
                       )
        
        # buttons 
        for info in [("Search", 0, self.search), ("Generate Password", 2, self.generate_pass), ("Add", 3, self.save_info)]:
            button = ctk.CTkButton(bottom, 
                                    text_color="black",
                                    font=FONT_LABEL,
                                    fg_color="white",
                                    text=info[0],
                                    command=info[2],
                                    hover_color=GRAY,
                                    border_color=GRAY,
                                    border_width=1
                                    )
            button.grid(row=info[1], 
                        column = 1 if info[1] == 3 else 2, 
                        columnspan = 2 if info[1] == 3 else 1,
                        sticky="nswe",
                        padx=1,
                        pady=1
                        )
        
    def check_entries(self, *args):
        
        if args[0] == 'PY_VAR0':
            self.website = self.vars_dict["Website"].get()
        elif args[0] == 'PY_VAR1':      
            self.email = self.vars_dict["Email/Username"].get()
        elif args[0] == 'PY_VAR2':  
            self.password = self.vars_dict["Password"].get()
        
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
    def generate_pass(self):
        
        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_list = [random.choice(LETTERS) for _ in range(nr_letters)]
        password_list += [random.choice(SYMBOLS) for _ in range(nr_symbols)]  
        password_list += [random.choice(NUMBERS) for _ in range(nr_numbers)]

        random.shuffle(password_list)

        self.password = "".join(password_list)
        self.vars_dict["Password"].set(self.password)
        pyperclip.copy(self.password)
        
# ---------------------------- SAVE PASSWORD ------------------------------- #
    def save_info(self):
        
        if self.website and self.email and self.password:
            is_ok = messagebox.askyesno(title=self.website,
                                        message=f"These are the details entered:\n"
                                        f"Email: {self.email}\n"
                                        f"Password: {self.password}"
                                        )
            if is_ok:
                new_data = {
                    self.website: {
                        "email": self.email,
                        "password": self.password
                    }               
                }
                
                try:
                    with open(r"Projects\29- Password Manager Gui\Saved_Data.json", "r") as file:
                        # Reading old data
                        data = json.load(file)
                        # updating old data
                        data.update(new_data)
                except FileNotFoundError:
                    data = new_data
                finally:
                    with open(r"Projects\29- Password Manager Gui\Saved_Data.json", "w") as file:
                        # saving data
                        json.dump(data, file, indent=4) 
                        for var in self.vars_dict:
                            if var != "Email/Username":
                                self.vars_dict[var].set("")
                
        else:
            messagebox.showinfo(title="Oops",
                                message="Please don't leave any fields empty!"
                                )

# ----------------------------- SEARCH EMAIL ------------------------------- #
    def search(self):
        
        if self.website:
            try:
                with open(r"Projects\29- Password Manager Gui\Saved_Data.json", "r") as file:
                    data = json.load(file)
            except: 
                messagebox.showinfo(title=f"Error",
                                message=f"No Data File Found."
                                )
            else:
                if self.website in data:
                        email = data[self.website]["email"]
                        password = data[self.website]["password"]
                        messagebox.showinfo(title=f"{self.website}",
                                    message=f"Email: {email}\n"
                                            f"Password: {password}"
                                    )
                else:
                    messagebox.showinfo(title=f"Error",
                                message=f"No Details for {self.website} exist"
                                )
        else:
            messagebox.showinfo(title="Oops",
                                message="Please enter a name for the Website to search"
                                )
            
if __name__ == '__main__':
    app = App()
    