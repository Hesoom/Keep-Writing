from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from utils import relative_to_assets
from startpage import StartPage
from goalpage import GoalPage
from typingpage import TypingPage

from tkinter import Tk, Canvas, Button

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1065x697")
        self.resizable(False, False)
        self.current_page = None
        self.goal = 5
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


if __name__ == "__main__":
    app = App()
    app.mainloop()