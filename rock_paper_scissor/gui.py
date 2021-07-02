import random
import tkinter as tk

LARGE_FONT = ("Verdana", 12)

# Images
rock_img = "imgs/rock.png"
paper_img = "imgs/paper.png"
scissors_img = "imgs/scissor.png"
human_img = "imgs/human.png"
computer_img = "imgs/robot.png"
win_human_img = "imgs/human_biceps.png"
win_computer_img = "imgs/robot_biceps.png"


class Game():

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
        return self.player_choice

    def computer_input(self):
        self.computer_choice = random.choice(self.choices)
        return self.computer_choice

    def compare_choices(self, player_choice, computer_choice):
        self.match = [player_choice, computer_choice]
        if len(set(self.match)) == 1:
            return "tie"
        elif self.match in self.victory:
            self.player_score += 1
            return "playerwin"
        else:
            self.computer_score += 1
            return "computerwin"

    def play(self, command):
        player = self.player_input(command)
        computer = self.computer_input()
        result = self.compare_choices(
            player, computer)
        #print(player, computer)
        return result, player, computer


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

        for F in (StartPage, PlayerVsComputer, ComputerVsComputer, ComputerWins, PlayerWins, Tie):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()

    def access_page(self, page):
        return self.frames[page]


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
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
        self.controller = controller
        self.result = ["result"]
        self.player_choice = tk.StringVar()
        self.computer_choice = tk.StringVar()
        self.player_score = tk.IntVar()
        self.computer_score = tk.IntVar()

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Player VS computer", font=LARGE_FONT)
        label.grid(columnspan=5)

        self.rock_img = tk.PhotoImage(file=rock_img)
        self.paper_img = tk.PhotoImage(file=paper_img)
        self.scissors_img = tk.PhotoImage(file=scissors_img)

        rock_btn = tk.Button(self, text="Rock!",
                             image=self.rock_img, compound="bottom", command=lambda: self.button_press(game.play, "rock"))

        paper_btn = tk.Button(self, text="Paper!",
                              image=self.paper_img, compound="bottom", command=lambda: self.button_press(game.play, "paper"))

        scissors_btn = tk.Button(
            self, text="Scissors!", image=self.scissors_img, compound="bottom", command=lambda: self.button_press(game.play, "scissor"))

        rock_btn.grid(row=1, column=1)
        paper_btn.grid(row=1, column=2)
        scissors_btn.grid(row=1, column=3)

        startpage_btn = tk.Button(self, text="Back to start page",
                                  command=lambda: controller.show_frame(StartPage))
        startpage_btn.grid(columnspan=5)

        self.grid_columnconfigure((0, 4), weight=1)

    def button_press(self, function, *args):
        """
        Handle the result of player's choice
        """
        game = Game()
        value = function(*args)
        self.result[0] = value[0]
        self.player_choice.set(value[1])
        self.computer_choice.set(value[2])

        if self.result[0] == "computerwin":
            app.show_frame(ComputerWins)
        elif self.result[0] == "playerwin":
            app.show_frame(PlayerWins)
        else:
            app.show_frame(Tie)
        print(self.player_choice, self.computer_choice)
        return self.player_choice, self.computer_choice


class ComputerWins(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller

        game = Game()

        choices = self.controller.access_page(PlayerVsComputer)
        player_choice = choices.player_choice
        computer_choice = choices.computer_choice

        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self, text="Computer Won!", font=LARGE_FONT)
        label.grid(columnspan=5, pady=10, padx=10)
        self.computer_win_img = tk.PhotoImage(
            file=win_computer_img).subsample(2, 2)
        computer_arm = tk.Label(self, image=self.computer_win_img)
        computer_arm.grid(columnspan=5, pady=10)
        again_btn = tk.Button(
            self, text="Play Again", command=lambda: controller.show_frame(PlayerVsComputer))
        again_btn.grid(columnspan=5, pady=10)
        startpage_btn = tk.Button(self, text="Back to start page",
                                  command=lambda: controller.show_frame(StartPage))
        startpage_btn.grid(columnspan=5, pady=10)
        label1 = tk.Label(self, text="You Played: ")
        label1.grid(row=6, column=1, pady=10)
        choices_lbl = tk.Label(
            self, textvariable=player_choice)
        choices_lbl.grid(row=6, column=2, pady=10)
        label2 = tk.Label(self, text="Computer Played: ")
        label2.grid(row=7, column=1, pady=10)
        choices2_lbl = tk.Label(
            self, textvariable=computer_choice)
        choices2_lbl.grid(row=7, column=2, pady=10)
        self.grid_columnconfigure((0, 4), weight=1)


class PlayerWins(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self, text="You Won!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self.player_win_img = tk.PhotoImage(file=win_human_img)
        player_arm = tk.Label(self, image=self.player_win_img)
        player_arm.pack(pady=10)
        again_btn = tk.Button(
            self, text="Play Again", command=lambda: controller.show_frame(PlayerVsComputer))
        again_btn.pack(pady=10)
        startpage_btn = tk.Button(self, text="Back to start page",
                                  command=lambda: controller.show_frame(StartPage))
        startpage_btn.pack(pady=10)


class Tie(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self, text="It's a Tie!", font=LARGE_FONT)
        label.grid(columnspan=5)
        self.computer_win_img = tk.PhotoImage(
            file=win_computer_img).subsample(2, 2)
        computer_arm = tk.Label(self, image=self.computer_win_img)
        computer_arm.grid(row=1, column=2, pady=10, padx=40)
        self.player_win_img = tk.PhotoImage(file=win_human_img)
        player_arm = tk.Label(self, image=self.player_win_img)
        player_arm.grid(row=1, column=3, pady=10, padx=40)
        again_btn = tk.Button(
            self, text="Play Again", command=lambda: controller.show_frame(PlayerVsComputer))
        again_btn.grid(columnspan=5, pady=10)
        startpage_btn = tk.Button(self, text="Back to start page",
                                  command=lambda: controller.show_frame(StartPage))
        startpage_btn.grid(columnspan=5, pady=10)
        self.grid_columnconfigure((0, 4), weight=1)


class ComputerVsComputer(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self, text="Computer VS computer", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        startpage_btn = tk.Button(self, text="Back to start page",
                                  command=lambda: controller.show_frame(StartPage))
        startpage_btn.pack()


if __name__ == "__main__":
    app = RockPaperScissors()
    app.mainloop()
