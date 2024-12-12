# ---------------------------- IMPORTS ------------------------------- #
import customtkinter as ctk
import tkinter as tk
from PIL import Image
from quiz_brain import QuizBrain

# ---------------------------- CONSTANTS ------------------------------- #
THEME_COLOR = "#375362"
WINDOW_WIDTH, WINDOW_HEIGHT = 350, 500
FONT_QUESTION = ("Arial", 35, "italic")
FONT_SCORE = ("Arial", 18, "bold")

# ---------------------------- UI SETUP ------------------------------- #
class QuizInterface(ctk.CTk):
    def __init__(self, quiz_brain: QuizBrain):
        super().__init__(fg_color=THEME_COLOR)
        
        # setup
        self._set_appearance_mode("light")
        self.iconbitmap(r"Projects\25- Gui Quiz App\images\empty.ico")
        self.title('Quizzler')
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False, False)
        self.quiz_brain = quiz_brain
        self.init_essentials()
        self.load_question()
        self.make_layout()
        
        # events
        self.bind("<Escape>", lambda event: self.destroy())
        
        # run
        self.mainloop()
        
    def init_essentials(self):
        
        # importing images
        tick_img = Image.open(r"Projects\25- Gui Quiz App\images\true.png")
        self.tick_image = ctk.CTkImage(tick_img, tick_img, size=(75, 75))
        
        cross_img = Image.open(r"Projects\25- Gui Quiz App\images\false.png")
        self.cross_image = ctk.CTkImage(cross_img, cross_img, size=(75, 75))
        
        # vars
        self.score_var = tk.StringVar(value=f"Score: {self.quiz_brain.score}")
        self.question_text = None
        
    def make_layout(self):
        
        self.rowconfigure(0, weight=1, uniform="a")
        self.rowconfigure(1, weight=4, uniform="a")
        self.rowconfigure(2, weight=2, uniform="a")
        self.columnconfigure((0,1), weight=1, uniform="a")
        
        self.tick_button = ctk.CTkButton(self, 
                                     corner_radius=0,
                                     fg_color="transparent",
                                     hover=False,
                                     text="",
                                     border_width=1,
                                     width=80,
                                     height=80,
                                     image=self.tick_image,
                                     command= lambda: self.check_answer("true")
                                     )
        self.tick_button.grid(row=2, column=0, padx=18, pady=10, sticky="e")
        
        self.cross_button = ctk.CTkButton(self, 
                                     corner_radius=0,
                                     fg_color="transparent",
                                     hover=False,
                                     text="",
                                     border_width=1,
                                     width=80,
                                     height=80,
                                     image=self.cross_image,
                                     command= lambda: self.check_answer("false"),
                                     )
        self.cross_button.grid(row=2, column=1, padx=18, pady=10, sticky="w")
        
        score_label = ctk.CTkLabel(self,
                                   fg_color="transparent",
                                   text_color="white",
                                   textvariable=self.score_var,
                                   font=FONT_SCORE
                                   )
        score_label.grid(row=0, column=1)
        
        self.canvas = tk.Canvas(self, highlightthickness=0, background="white")
        self.canvas.grid(row=1, column=0, columnspan=2, padx=40, pady=30, sticky="nswe")
        self.canvas_text = self.canvas.create_text(40, 250, 
                                              font=FONT_QUESTION, 
                                              text=self.question_text,
                                              anchor="w",
                                              width=750
                                              )
     
    def load_question(self):
        if self.quiz_brain.still_has_questions():
            self.question_text = self.quiz_brain.next_question()
            if self.quiz_brain.question_number > 1:
                self.canvas.itemconfigure(self.canvas_text, text=self.question_text)
        else:
            final_msg = f"You've reached the end of the quiz.\nYour Final Score: {self.quiz_brain.score}/10"
            self.canvas.itemconfig(self.canvas_text, text=final_msg)
            self.tick_button.configure(state="disabled")
            self.cross_button.configure(state="disabled")
            
    def check_answer(self, answer):
        user_answer = self.quiz_brain.check_answer(answer)
        self.give_feedback(user_answer)
        self.score_var.set(f"Score: {self.quiz_brain.score}")
        
    def give_feedback(self, user_answer):
        color = "green" if user_answer else "red"
        self.canvas.configure(background=color)
        self.after(800, self.restore_canvas_bg)
            
    def restore_canvas_bg(self):
        self.canvas.configure(background="white")
        self.load_question()
    