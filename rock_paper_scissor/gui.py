import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)

# Images
rock_img = "imgs/rock.png"
paper_img = "imgs/paper.png"
scissors_img = "imgs/scissor.png"
human_img = "imgs/human.png"
computer_img = "imgs/robot.png"
win_human_img = "imgs/human_biceps.png"
win_computer_img = "imgs/robot_biceps.png"


class RockPaperScissors(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Rock Paper Scissors")

        # Define container
        container = tk.Frame(self)
        container.pack(side="top", fill="none", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PlayerVsComputer, ComputerVsComputer):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Rock Paper Scissor", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        self.human_img = tk.PhotoImage(file=human_img)
        self.computer_img = tk.PhotoImage(file=computer_img)

        player_computer_btn = tk.Button(
            self, text="       Play against your computer       ", image=self.human_img, command=lambda: controller.show_frame(PlayerVsComputer), compound="bottom")

        player_computer_btn.pack(side="left")

        computer_computer_btn = tk.Button(self, text="Watch your computer play against himself", image=self.computer_img,
                                          command=lambda: controller.show_frame(ComputerVsComputer), compound="bottom")
        computer_computer_btn.pack(side="left")


class PlayerVsComputer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Player VS computer", font=LARGE_FONT)
        label.grid(columnspan=5)

        self.rock_img = tk.PhotoImage(file=rock_img)
        self.paper_img = tk.PhotoImage(file=paper_img)
        self.scissors_img = tk.PhotoImage(file=scissors_img)

        rock_btn = tk.Button(self, text="Rock!",
                             image=self.rock_img, compound="bottom")
        paper_btn = tk.Button(self, text="Paper!",
                              image=self.paper_img, compound="bottom")
        scissors_btn = tk.Button(
            self, text="Scissors!", image=self.scissors_img, compound="bottom")

        rock_btn.grid(row=1, column=1)
        paper_btn.grid(row=1, column=2)
        scissors_btn.grid(row=1, column=3)

        startpage_btn = tk.Button(self, text="Back to start page",
                                  command=lambda: controller.show_frame(StartPage))
        startpage_btn.grid(columnspan=5)

        human_score = tk.Label(self, text="Your Score: 0")
        computer_score = tk.Label(self, text="Computer Score: 0")
        human_score.grid(columnspan=5)
        computer_score.grid(columnspan=5)

        self.grid_columnconfigure((0, 4), weight=1)


class ComputerVsComputer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self, text="Computer VS computer", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        startpage_btn = tk.Button(self, text="Back to start page",
                                  command=lambda: controller.show_frame(StartPage))
        startpage_btn.pack()


app = RockPaperScissors()
app.mainloop()
