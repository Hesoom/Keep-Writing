from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from utils import relative_to_assets

class StartPage:
    def __init__(self, root):
        self.root = root
        

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
        self.start_page_image = PhotoImage(
            file=relative_to_assets("startpage.png"))
        self.start_page = self.canvas.create_image(
            533.0,
            348.0,
            image=self.start_page_image
        )

        self.start_btn_image = PhotoImage(
            file=relative_to_assets("start_btn.png"))
        self.start_btn = Button(
            image=self.start_btn_image,
            borderwidth=0,
            highlightthickness=0,
            command=root.show_typing_page,
            relief="flat",
            bg='white'
        )
        self.start_btn.place(
            x=433.0,
            y=364.0,
            width=199.0,
            height=40.0
        )

        self.goal_btn_image = PhotoImage(
            file=relative_to_assets("goal_btn.png"))
        self.goal_btn = Button(
            image=self.goal_btn_image,
            borderwidth=0,
            highlightthickness=0,
            command=root.show_goal_page,
            relief="flat",
            bg='white'
        )
        self.goal_btn.place(
            x=433.0,
            y=422.0,
            width=199.0,
            height=40.0
        )


    def destroy(self):
        self.canvas.destroy()
        self.start_btn.destroy()
        self.goal_btn.destroy()
