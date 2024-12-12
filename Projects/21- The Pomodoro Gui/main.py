
# ---------------------------- CONSTANTS ------------------------------- #
WINDOW_WIDTH, WINDOW_HEIGHT = 400, 325
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BUTTON_HOVER = "#e6e5dc"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- IMPORTS ---------------------------------- #
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import time
from math import floor

# ---------------------------- MAIN APP --------------------------------- #
class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color = YELLOW)
        
        # window setup
        self._set_appearance_mode("light")
        self.iconbitmap(r"Projects\28- The Pomodoro Gui\empty.ico")
        self.title('Pomodoro')
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False, False)
        self.place_widgets()
        
        # laps
        self.lap = 0
        self.lap_done = tk.BooleanVar(value=False)
        self.lap_done.trace_add("write", self.lap_end_checker)
        self.after_id = None
        
        # events
        self.bind("<Escape>", lambda event: self.destroy())

        # run
        self.mainloop()
        
    # ---------------------------- UI SETUP ------------------------------- #
    def place_widgets(self):

        # layout
        self.rowconfigure(0, weight=1, uniform="a")
        self.rowconfigure(1, weight=3, uniform="a")
        self.rowconfigure(2, weight=1, uniform="a")
        self.columnconfigure(0, weight=1, uniform="a")
        
        # top label
        self.main_label = ctk.CTkLabel(self, 
                             text_color=GREEN,
                             font=(FONT_NAME, 45, "bold"),
                             anchor="center",
                             text="Timer",
                             )
        self.main_label.grid(row=0, column=0, padx=20)
        
        # canvas 
        self.time = tk.StringVar(value="00:00")
        self.canvas = tk.Canvas(self, bg=YELLOW, highlightthickness=0)
        img = Image.open(r"Projects\28- The Pomodoro Gui\tomato.png")
        size = img.size
        self.tomato_img = ImageTk.PhotoImage(image=img.resize((size[0]*2, size[1]*2)))
        self.canvas.create_image(WINDOW_WIDTH + 100, WINDOW_HEIGHT - 95, image=self.tomato_img)
        self.timer_text = self.canvas.create_text(WINDOW_WIDTH + 100, WINDOW_HEIGHT - 40, text="00:00", fill="white", font=(FONT_NAME, 70, "bold"))
        self.canvas.grid(row=1, column=0, sticky="nsew")
        
        # bottom stuff
        bottom = ctk.CTkFrame(self, fg_color="transparent")
        bottom.grid(row=2, column=0, sticky="nswe")
        bottom.rowconfigure(0, weight=1, uniform="b")
        bottom.columnconfigure((0,1,2), weight=1, uniform="b")
        
        # buttons
        start = ctk.CTkButton(bottom, 
                              fg_color="white", 
                              hover_color=BUTTON_HOVER,
                              text_color="black",
                              text="Start",
                              anchor="right",
                              font=("Callibri", 13, "bold"),
                              command=lambda: self.lap_handler(), # self.countdown_timer(1), # self.lap_handler(),
                              width=50
                              )
        start.grid(row=0, column=0, sticky="ne", padx=30)
        
        reset = ctk.CTkButton(bottom, 
                              fg_color="white", 
                              hover_color=BUTTON_HOVER,
                              text_color="black",
                              text="Reset",
                              anchor="left",
                              font=("Callibri", 13, "bold"),
                              command=lambda: self.reset_all(),
                              width=50
                              )
        reset.grid(row=0, column=2, sticky="nw", padx=30)
        
        # check label
        self.check_text = tk.StringVar()
        check = ctk.CTkLabel(bottom,
                             textvariable=self.check_text,
                             text_color=GREEN
                             )
        check.grid(row=0, column=1, sticky="n", pady=15)
        
    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
    def countdown_timer(self, time_in_mins):
        
        time_in_secs = time_in_mins * 60
        mins = int(time_in_secs // 60)
        secs = int(time_in_secs % 60)
        if secs < 10:
            secs = f"0{secs}"
        if mins < 10:
            mins = f"0{mins}"
        text = f"{mins}:{secs}"
        self.canvas.itemconfig(self.timer_text, text=text)
        if time_in_secs > 0:
            self.after_id = self.after(1000, self.countdown_timer, (time_in_secs - 1)/60)
        else: 
            self.lap_done.set(True)
    
    # ---------------------------- TIMER MECHANISM ------------------------------- #    
    def lap_handler(self):
        
        self.lap += 1
            
        if self.lap > 1 and self.lap % 2 == 0:
            check_count = self.lap // 2
            self.check_text.set(f"✔" * check_count)
        
        if self.lap in [1, 3, 5, 7]: # work laps
            if self.lap == 1:
                self.check_text.set("")
            self.main_label.configure(text="Work", text_color=GREEN)
            time_in_mins = WORK_MIN
            self.countdown_timer(time_in_mins)
        elif self.lap in [2, 4, 6]: # break laps
            self.main_label.configure(text="Break", text_color=RED)
            time_in_mins = SHORT_BREAK_MIN
            self.countdown_timer(time_in_mins)
        elif self.lap == 8: # long break lap
            self.main_label.configure(text="Break", text_color=PINK)
            time_in_mins = LONG_BREAK_MIN
            self.countdown_timer(time_in_mins)
        else: # end timer
            self.main_label.configure(text="Timer", text_color=GREEN)
            self.lap = 0
        
    def lap_end_checker(self, *args):
        if self.lap_done.get():
            self.lap_done.set(False)
            self.lap_handler()
            
    # ---------------------------- TIMER RESET ------------------------------- # 
    def reset_all(self):
        if self.after_id:
            self.main_label.configure(text="Timer", text_color=GREEN)
            self.lap = 0
            self.lap_done.set(False)
            self.check_text.set("")
            text = f"00:00"
            self.canvas.itemconfig(self.timer_text, text=text)
            self.after_cancel(self.after_id)

if __name__ == '__main__':
    app = App()
    