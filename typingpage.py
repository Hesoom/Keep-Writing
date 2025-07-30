from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Label, filedialog
from utils import relative_to_assets


class TypingPage:
    def __init__(self, root):
        self.root = root
        self.remaining_time = self.root.goal * 60
        self.stop_timer = 5
        self.after_id = None

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
            wrap="word",
            bd=0,
            bg="#FFFFFF",
            fg="#929292",
            highlightthickness=0,
            font=("arial",16)
        )
        self.entry.insert("1.0", "Start Typing ...")
        self.entry.focus()
        self.entry.mark_set("insert", "%d.%d" % (0,0))
        self.entry.place(
            x=259.0,
            y=78.0,
            width=548.0,
            height=480.0
        )

        self.started_typing = False
        self.typing = False
        self.entry.bind("<Key>", self.on_key_press)

        self.timer_label = Label(root, text=f"0{self.root.goal}:00" if self.root.goal==5 else f"{self.root.goal}:00", font=("Arial", 35),bg="#FFFFFF",fg="#D3D3D3")
        self.timer_label.place(x=680, y=570)

        self.back_btn_image = PhotoImage(
            file=relative_to_assets("back_btn.png"))
        self.back_btn = Button(
            image=self.back_btn_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.root.show_start_page,
            relief="flat",
            activebackground='white',
            bg='white'
        )
        self.back_btn.place(
            x=270,
            y=580,
            width=160.0,
            height=39.0
        )

        self.status_label = Label(root, text="", fg="black", font=("Arial",14,'italic'))

    def on_key_press(self,event):
        
        if not self.started_typing:
            self.started_typing = True
            self.entry.delete("1.0", 'end')
            self.entry.config(fg="#2C2C2C")
            self.update_timer()

        self.entry.config(fg="#353535")

        self.stop_timer = 5
        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
        self.after_id = self.root.after(1000, self.update_delete_timer)

    def update_timer(self):
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
        self.remaining_time -= 1
        if self.remaining_time >= 0:
            self.root.after(1000, self.update_timer)
        else:
            self.finish()
    
    def update_delete_timer(self):
        self.stop_timer -= 1
        if self.stop_timer >= 0:
            if self.stop_timer == 0:
                self.time_over()
            elif self.stop_timer < 2:
                self.entry.config(fg="#E0E0E0")
            elif self.stop_timer < 3:
                self.entry.config(fg="#B1B1B1")
            elif self.stop_timer < 4:
                self.entry.config(fg="#808080")    

            self.after_id = self.root.after(1000, self.update_delete_timer)

    def time_over(self):
        self.entry.place_forget()
        self.timer_label.place_forget()

        self.lost_page_image = PhotoImage(
            file=relative_to_assets("lostpage.png"))
        self.lost_page = self.canvas.create_image(
            533.0,
            348.0,
            image=self.lost_page_image
        )

        self.back_btn_image = PhotoImage(
            file=relative_to_assets("back_btn.png"))
        self.back_btn = Button(
            image=self.back_btn_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.root.show_start_page,
            relief="flat",
            activebackground='white',
            bg='white'
        )
        self.back_btn.place(
            x=453.0,
            y=385.0,
            width=160.0,
            height=39.0
        )


    def finish(self):
        self.entry_text = self.entry.get("1.0", "end-1c")
        self.entry.place_forget()
        self.timer_label.place_forget()

        self.finish_page_image = PhotoImage(
            file=relative_to_assets("finishpage.png"))
        self.typing_page = self.canvas.create_image(
            533.0,
            348.0,
            image=self.finish_page_image
        )

        self.save_btn_image = PhotoImage(
            file=relative_to_assets("save_btn.png"))
        self.save_btn = Button(
            image=self.save_btn_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.save_entry_to_file,
            relief="flat",
            activebackground='white',
            bg='white'
        )
        self.save_btn.place(
            x=453.0,
            y=367.0,
            width=160.0,
            height=39.0
        )

        self.back_btn_image = PhotoImage(
            file=relative_to_assets("back_btn.png"))
        self.back_btn = Button(
            image=self.back_btn_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.root.show_start_page,
            relief="flat",
            activebackground='white',
            bg='white'
        )
        self.back_btn.place(
            x=453.0,
            y=421.0,
            width=160.0,
            height=39.0
        )


    def save_entry_to_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:  # If a file path is selected
            
            try:
                with open(file_path, "w") as file:
                    file.write(self.entry_text)
                self.status_label.config(text=f"Data saved!", bg="#A7FFAB")
                self.status_label.place(x=10,y=10)
            except Exception as e:
                self.status_label.config(text=f"Error saving file: {e}", bg="#FFA7A7")
                self.status_label.place(x=10,y=10)

    def destroy(self):
        self.canvas.destroy()
        self.entry.destroy()