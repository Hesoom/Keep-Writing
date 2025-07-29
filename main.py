from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from utils import relative_to_assets


from tkinter import Tk, Canvas, Button

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1065x697")
        self.resizable(False, False)
        self.current_page = None
        self.show_start_page()

    def show_start_page(self):
        self._switch_page(StartPage)

    def show_goal_page(self):
        self._switch_page(GoalPage)

    def show_typing_page(self):
        self._switch_page(TypingPage)

    def _switch_page(self, page_class):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = page_class(self)

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



class GoalPage:
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
        self.goal_page_image = PhotoImage(
            file=relative_to_assets("page.png"))
        self.goal_page = self.canvas.create_image(
            533.0,
            348.0,
            image=self.goal_page_image
        )

        self.btn_5_image = PhotoImage(
            file=relative_to_assets("5_btn.png"))
        self.btn_5 = Button(
            image=self.btn_5_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat",
            bg='white'
        )
        self.btn_5.place(
            x=336.0,
            y=290.0,
            width=46.0,
            height=46.0
        )

        self.btn_15_image = PhotoImage(
            file=relative_to_assets("15_btn.png"))
        self.btn_15 = Button(
            image=self.btn_15_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_15 clicked"),
            relief="flat",
            bg='white'
        )
        self.btn_15.place(
            x=423.0,
            y=290.0,
            width=46.0,
            height=46.0
        )

        self.btn_30_image = PhotoImage(
            file=relative_to_assets("30_btn.png"))
        self.btn_30 = Button(
            image=self.btn_30_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_30 clicked"),
            relief="flat",
            bg='white'
        )
        self.btn_30.place(
            x=510.0,
            y=290.0,
            width=46.0,
            height=46.0
        )

        self.btn_45_image = PhotoImage(
            file=relative_to_assets("45_btn.png"))
        self.btn_45 = Button(
            image=self.btn_45_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_45 clicked"),
            relief="flat",
            bg='white'
        )
        self.btn_45.place(
            x=597.0,
            y=290.0,
            width=46.0,
            height=46.0
        )

        self.btn_60_image = PhotoImage(
            file=relative_to_assets("60_btn.png"))
        self.btn_60 = Button(
            image=self.btn_60_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_60 clicked"),
            relief="flat",
            bg='white'
        )
        self.btn_60.place(
            x=684.0,
            y=290.0,
            width=46.0,
            height=46.0
        )



        self.start_btn_image2 = PhotoImage(
            file=relative_to_assets("start_btn2.png"))
        self.start_btn2 = Button(
            image=self.start_btn_image2,
            borderwidth=0,
            highlightthickness=0,
            command=root.show_typing_page,
            relief="flat",
            bg='white'
        )
        self.start_btn2.place(
            x=453.0,
            y=368.0,
            width=160.0,
            height=39.0
        )

    def destroy(self):
        self.canvas.destroy()
        self.btn_5.destroy()
        self.btn_15.destroy()
        self.btn_30.destroy()
        self.btn_45.destroy()
        self.btn_60.destroy()
        self.start_btn2.destroy()


class TypingPage:
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

    def destroy(self):
        self.canvas.destroy()
        self.entry.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()