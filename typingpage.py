from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Label
from utils import relative_to_assets


class TypingPage:
    def __init__(self, root):
        self.root = root
        
        self.remaining_time = self.root.goal * 60

        self.canvas = Canvas(
            root,
            bg = "#E4E4E4",
            height = 697,
            width = 1065,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.typing_page_image = PhotoImage(
            file=relative_to_assets("page.png"))
        self.typing_page = self.canvas.create_image(
            533.0,
            348.0,
            image=self.typing_page_image
        )


        self.entry = Text(
            bd=0,
            bg="#FFFFFF",
            fg="#6D6D6D",
            highlightthickness=0,
            font=("arial",16)
        )
        self.entry.place(
            x=259.0,
            y=78.0,
            width=548.0,
            height=540.0
        )

        self.timer_label = Label(root, text=f"0{self.root.goal}:00" if self.root.goal==5 else f"{self.root.goal}:00", font=("Arial", 24, 'bold'),bg='#E4E4E4',fg="#969696")
        self.timer_label.place(x=910, y=85)
    
    def update_timer(self):
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60

        self.timer_label.config(text=f"{minutes:02}:{seconds:02}")

        self.remaining_time -= 1

        if self.remaining_time >= 0:
            self.root.after(1000, self.update_timer)

    def destroy(self):
        self.canvas.destroy()
        self.entry.destroy()