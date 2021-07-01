import random
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


class Game(object):

    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.victory = [
            ['rock', 'scissors'],
            ['paper', 'rock'],
            ['scissors', 'paper']
        ]
        self.player_score = 0
        self.computer_score = 0

    def _get_rules(self, list_of_rules):
        self.choices.extend(list(set(list_of_rules)))
        self.victory.extend(list_of_rules)

    def player_input(self, command):
        self.player_choice = command
        print(self.player_choice)
        return self.player_choice

    def computer_input(self):
        self.computer_choice = random.choice(self.choices)
        return self.computer_choice

    def compare_choices(self, player_choice, computer_choice):
        match = [player_choice, computer_choice]
        # if len(set(match)) == 1:


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
        game = Game()
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Player VS computer", font=LARGE_FONT)
        label.grid(columnspan=5)

        self.rock_img = tk.PhotoImage(file=rock_img)
        self.paper_img = tk.PhotoImage(file=paper_img)
        self.scissors_img = tk.PhotoImage(file=scissors_img)

        rock_btn = tk.Button(self, text="Rock!",
                             image=self.rock_img, compound="bottom", command=lambda *args: game.player_input("rock"))

        paper_btn = tk.Button(self, text="Paper!",
                              image=self.paper_img, compound="bottom", command=lambda *args: game.player_input("paper"))
        scissors_btn = tk.Button(
            self, text="Scissors!", image=self.scissors_img, compound="bottom", command=lambda *args: game.player_input("scissors"))

        rock_btn.grid(row=1, column=1)
        paper_btn.grid(row=1, column=2)
        scissors_btn.grid(row=1, column=3)

        startpage_btn = tk.Button(self, text="Back to start page",
                                  command=lambda: controller.show_frame(StartPage))
        startpage_btn.grid(columnspan=5)

        human_score = tk.Label(self, text=f"Your Score: {game.player_score}")
        computer_score = tk.Label(
            self, text=f"Computer Score: {game.computer_score}")
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
