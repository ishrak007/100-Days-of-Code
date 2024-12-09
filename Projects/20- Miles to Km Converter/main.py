import customtkinter as ctk
import tkinter as tk

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color = "white")
        
        # window setup
        self._set_appearance_mode("light")
        self.iconbitmap(r"Projects\27- Miles to Km Converter\empty.ico")
        self.title('Miles to Km Converter')
        self.geometry('300x150')
        self.resizable(False, False)

        # layout
        self.columnconfigure(0, weight = 1, uniform="a")
        self.columnconfigure((1,2,3), weight = 2, uniform="a")
        self.rowconfigure(0, weight = 1, uniform = 'a')
        
        
        self.place_widgets()
        
        # events
        self.bind("<Escape>", lambda event: self.destroy())

        # run
        self.mainloop()
        
    def place_widgets(self):
        
        font = ctk.CTkFont(family="callibri", size=15)
        
        # col 1
        col_1 = ctk.CTkFrame(self, fg_color="transparent") 
        col_1.grid(row=0, column=1, sticky="e", padx=7)
        label_1 = ctk.CTkLabel(col_1, 
                               text="is equal to",
                               text_color="black",
                               font=font
                               )
        label_1.pack(side="right")

        # col 2
        col_2 = ctk.CTkFrame(self, fg_color="transparent") 
        col_2.grid(row=0, column=2)
        col_2.rowconfigure((0,1,2,3,4), weight = 1, uniform="b")
        col_2.columnconfigure(0, weight = 1, uniform="b")
        
        # input text
        self.text_var = tk.StringVar()
        text = ctk.CTkEntry(col_2, 
                              text_color="black",
                              border_color="#8f9adb",
                              textvariable=self.text_var,
                              corner_radius=0,
                              fg_color="transparent",
                              font=font
                              )
        text.grid(row=0, column=0, rowspan=2, sticky="s")

        # output label
        self.result_str = tk.StringVar(value="0")
        result = ctk.CTkLabel(col_2, 
                              text_color="black",
                              font=font,
                              textvariable=self.result_str
                              )
        result.grid(row=2, column=0)

        # button
        calc = ctk.CTkButton(col_2,
                             text_color="black",
                             hover_color="#daddeb",
                             text="Calculate",
                             fg_color="white",
                             font=font,
                             command=lambda: self.process_input(self.text_var.get())
                             )
        calc.grid(row=3, column=0, rowspan=2, sticky="n")
        
        
        # col 3
        col_3 = ctk.CTkFrame(self, fg_color="transparent") 
        col_3.grid(row=0, column=3, sticky="nswe", padx=12)
        col_3.rowconfigure((0,1,2,3,4), weight = 1, uniform="c")
        col_3.columnconfigure(0, weight = 1, uniform="c")
        
        # miles
        miles = ctk.CTkLabel(col_3, 
                     text="Miles", 
                     text_color="black",
                     font=font
                     )
        miles.grid(row=0, column=0, rowspan=2, sticky="sw")
        
        # km
        km = ctk.CTkLabel(col_3, 
                     text="Km", 
                     text_color="black",
                     font=font
                     )
        km.grid(row=2, column=0, sticky="w")
        
    def process_input(self, input_txt):
        
        try:
            miles = float(input_txt)
            self.calculate(miles)
        except:
            pass
        
    def calculate(self, miles):
        
        km = miles * 1.60934
        result = f"{km:.2f}"
        self.result_str.set(result)

if __name__ == '__main__':
    app = App()
    