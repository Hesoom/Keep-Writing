from tkinter import Tk, Canvas, Button, PhotoImage
from utils import relative_to_assets

class GoalPage:
    def __init__(self, root):
        self.root = root
        self.selected_time = 5  # Default selection

        self.canvas = Canvas(
            root,
            bg="#E4E4E4",
            height=697,
            width=1065,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.goal_page_image = PhotoImage(
            file=relative_to_assets("page.png"))
        self.goal_page = self.canvas.create_image(
            533.0,
            348.0,
            image=self.goal_page_image
        )

        # Preload all button images
        self.btn_images = {
            5: {
                "normal": PhotoImage(file=relative_to_assets("5_btn.png")),
                "selected": PhotoImage(file=relative_to_assets("active_5_btn.png"))
            },
            15: {
                "normal": PhotoImage(file=relative_to_assets("15_btn.png")),
                "selected": PhotoImage(file=relative_to_assets("active_15_btn.png"))
            },
            30: {
                "normal": PhotoImage(file=relative_to_assets("30_btn.png")),
                "selected": PhotoImage(file=relative_to_assets("active_30_btn.png"))
            },
            45: {
                "normal": PhotoImage(file=relative_to_assets("45_btn.png")),
                "selected": PhotoImage(file=relative_to_assets("active_45_btn.png"))
            },
            60: {
                "normal": PhotoImage(file=relative_to_assets("60_btn.png")),
                "selected": PhotoImage(file=relative_to_assets("active_60_btn.png"))
            }
        }

        # Create buttons and place them
        self.goal_buttons = {}
        x_positions = {5: 336, 15: 423, 30: 510, 45: 597, 60: 684}

        for time, x in x_positions.items():
            image = (
                self.btn_images[time]["selected"]
                if time == self.selected_time
                else self.btn_images[time]["normal"]
            )
            btn = Button(
                image=image,
                borderwidth=0,
                highlightthickness=0,
                command=lambda t=time: self.clicked(t),
                relief="flat",
                bg='white',
                activebackground='white'
            )
            btn.place(x=x, y=290.0, width=46.0, height=46.0)
            self.goal_buttons[time] = btn

        # Start button
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

    def clicked(self, time):
        if time == self.selected_time:
            return

        # Update previous button to normal image
        prev_btn = self.goal_buttons[self.selected_time]
        prev_btn.config(image=self.btn_images[self.selected_time]["normal"])

        # Update new selected button to active image
        new_btn = self.goal_buttons[time]
        new_btn.config(image=self.btn_images[time]["selected"])

        self.root.goal = time
        print(f"Selected goal: {time} minutes")

    def destroy(self):
        self.canvas.destroy()
        for btn in self.goal_buttons.values():
            btn.destroy()
        self.start_btn2.destroy()
