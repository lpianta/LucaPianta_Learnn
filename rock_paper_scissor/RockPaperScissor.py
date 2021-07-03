import random
import tkinter as tk

LARGE_FONT = ("Verdana", 12)

# Images
rock_img = "imgs/rock.png"
paper_img = "imgs/paper.png"
scissors_img = "imgs/scissor.png"
player_img = "imgs/player.png"
computer_img = "imgs/robot.png"
win_player_img = "imgs/player_biceps.png"
win_computer_img = "imgs/robot_biceps.png"
computer1_img = "imgs/computer1.png"
computer2_img = "imgs/computer2.png"


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
        """
        Extend possible choices and rules
        """
        self.choices.extend(list(set(list_of_rules)))
        self.victory.extend(list_of_rules)

    def player_input(self, command):
        """
        Get player input
        """
        self.player_choice = command
        return self.player_choice

    def computer_input(self):
        """
        Get random computer input
        """
        self.computer_choice = random.choice(self.choices)
        return self.computer_choice

    def compare_choices(self, player_choice, computer_choice):
        """
        Check winner
        """
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
        """
        Play against computer
        """
        player = self.player_input(command)
        computer = self.computer_input()
        result = self.compare_choices(player, computer)
        return result, player, computer

    def computer_play(self):
        """
        Make computer play against himself
        """
        computer1 = self.computer_input()
        computer2 = self.computer_input()
        result = self.compare_choices(computer1, computer2)
        return result, computer1, computer2


class RockPaperScissors(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Rock Paper Scissors")

        # Define container
        container = tk.Frame(self)
        container.pack(side="top", fill="none", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Define frames
        self.frames = {}

        for F in (StartPage, PlayerVsComputer, ComputerVsComputer, ComputerWins, PlayerWins, Tie):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, controller):
        """
        Show a page
        """
        frame = self.frames[controller]
        frame.tkraise()

    def access_page(self, page):
        """
        Access a page attributes and methods
        """
        return self.frames[page]


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        game = Game()
        self.controller = controller

        # Initialize variables
        self.result = tk.StringVar()
        self.computer1_choice = tk.StringVar()
        self.computer2_choice = tk.StringVar()
        self.computer1_score = tk.IntVar()
        self.computer2_score = tk.IntVar()

        # Load images
        self.player_img = tk.PhotoImage(file=player_img)
        self.computer_img = tk.PhotoImage(file=computer_img)

        # Define labels
        title = tk.Label(self, text="Rock Paper Scissor", font=LARGE_FONT)

        # Define buttons
        player_computer_btn = tk.Button(
            self, text="       Play against your computer       ", image=self.player_img, command=lambda: controller.show_frame(PlayerVsComputer), compound="bottom")
        computer_computer_btn = tk.Button(self, text="Watch your computer play against himself", image=self.computer_img,
                                          command=lambda: self.computer_game(game.computer_play), compound="bottom")

        # Display
        title.pack(pady=10, padx=10)
        player_computer_btn.pack(side="left")
        computer_computer_btn.pack(side="left")

    def computer_game(self, function, *args):
        """
        Function to handle returns value (Tkinter specific)
        """
        value = function(*args)

        if value[0] == "playerwin":
            self.result.set("Computer 1 Won!")
            self.computer1_score.set(self.computer1_score.get() + 1)
        elif value[0] == "computerwin":
            self.result.set("Computer 2 Won!")
            self.computer2_score.set(self.computer2_score.get() + 1)
        elif value[0] == "tie":
            self.result.set("It's a tie!")

        self.computer1_choice.set(value[1])
        self.computer2_choice.set(value[2])
        app.show_frame(ComputerVsComputer)

        return self.result, self.computer1_choice, self.computer2_choice


class PlayerVsComputer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        game = Game()
        self.controller = controller

        # Initialize variables
        self.result = ["result"]
        self.player_choice = tk.StringVar()
        self.computer_choice = tk.StringVar()
        self.player_score = tk.IntVar()
        self.computer_score = tk.IntVar()

        # Load images
        self.rock_img = tk.PhotoImage(file=rock_img)
        self.paper_img = tk.PhotoImage(file=paper_img)
        self.scissors_img = tk.PhotoImage(file=scissors_img)

        # Define labels
        title = tk.Label(self, text="Player VS computer", font=LARGE_FONT)
        player_score_lbl = tk.Label(self, text="Your score: ")
        player_score_vl = tk.Label(self, textvariable=self.player_score)
        computer_score_lbl = tk.Label(self, text="Computer score: ")
        computer_score_vl = tk.Label(self, textvariable=self.computer_score)

        # Define buttons
        rock_btn = tk.Button(self, text="Rock!",
                             image=self.rock_img, compound="bottom", command=lambda: self.button_press(game.play, "rock"))
        paper_btn = tk.Button(self, text="Paper!",
                              image=self.paper_img, compound="bottom", command=lambda: self.button_press(game.play, "paper"))
        scissors_btn = tk.Button(
            self, text="Scissors!", image=self.scissors_img, compound="bottom", command=lambda: self.button_press(game.play, "scissor"))
        startpage_btn = tk.Button(self, text="Back to start page",
                                  command=lambda: [controller.show_frame(StartPage), self.player_score.set(0), self.computer_score.set(0)])

        # Display
        title.grid(columnspan=5, pady=10)
        rock_btn.grid(row=1, column=1, pady=10)
        paper_btn.grid(row=1, column=2, pady=10)
        scissors_btn.grid(row=1, column=3, pady=10)
        player_score_lbl.grid(columnspan=5, pady=10)
        player_score_vl.grid(columnspan=5)
        computer_score_lbl.grid(columnspan=5, pady=10)
        computer_score_vl.grid(columnspan=5)
        startpage_btn.grid(columnspan=5, pady=10)

        self.grid_columnconfigure((0, 4), weight=1)

    def button_press(self, function, *args):
        """
        Function to handle returns value (Tkinter specific)
        """
        value = function(*args)
        self.result[0] = value[0]
        self.player_choice.set(value[1])
        self.computer_choice.set(value[2])

        if self.result[0] == "computerwin":
            self.computer_score.set(self.computer_score.get() + 1)
            app.show_frame(ComputerWins)

        elif self.result[0] == "playerwin":
            self.player_score.set(self.player_score.get() + 1)
            app.show_frame(PlayerWins)

        else:
            app.show_frame(Tie)

        return self.player_choice, self.computer_choice


class ComputerWins(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Access PlayerVsComputer to get variables
        choices = self.controller.access_page(PlayerVsComputer)
        player_choice = choices.player_choice
        computer_choice = choices.computer_choice
        self.player_score = choices.player_score
        self.computer_score = choices.computer_score

        # Load image
        self.computer_win_img = tk.PhotoImage(
            file=win_computer_img).subsample(2, 2)

        # Define labels
        player_played_lbl = tk.Label(self, text="You Played: ")
        player_choice_lbl = tk.Label(
            self, textvariable=player_choice)
        comp_played_lbl = tk.Label(self, text="Computer Played: ")
        comp_choice_lbl = tk.Label(
            self, textvariable=computer_choice)
        winner_lbl = tk.Label(
            self, text="Computer Won!", font=LARGE_FONT)
        computer_arm = tk.Label(self, image=self.computer_win_img)
        player_score_lbl = tk.Label(self, text="Your score: ")
        player_score_vl = tk.Label(self, textvariable=self.player_score)
        computer_score_lbl = tk.Label(self, text="Computer score: ")
        computer_score_vl = tk.Label(self, textvariable=self.computer_score)

        # Define buttons
        again_btn = tk.Button(
            self, text="Play Again", command=lambda: controller.show_frame(PlayerVsComputer))
        startpage_btn = tk.Button(self, text="Back to start page",
                                  command=lambda: [controller.show_frame(StartPage), self.player_score.set(0), self.computer_score.set(0)])

        # Display
        player_played_lbl.grid(row=0, column=1)
        player_choice_lbl.grid(row=0, column=2)
        comp_played_lbl.grid(row=1, column=1)
        comp_choice_lbl.grid(row=1, column=2)
        winner_lbl.grid(row=2, columnspan=5, pady=10, padx=10)
        computer_arm.grid(row=3, columnspan=5, pady=10)
        player_score_lbl.grid(row=4, columnspan=5)
        player_score_vl.grid(row=5, columnspan=5)
        computer_score_lbl.grid(row=6, columnspan=5)
        computer_score_vl.grid(row=7, columnspan=5)
        again_btn.grid(row=8, columnspan=5, pady=10)
        startpage_btn.grid(row=9, columnspan=5)

        self.grid_columnconfigure((0, 4), weight=1)


class PlayerWins(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Access PlayerVsComputer to get variables
        choices = self.controller.access_page(PlayerVsComputer)
        player_choice = choices.player_choice
        computer_choice = choices.computer_choice
        self.player_score = choices.player_score
        self.computer_score = choices.computer_score

        # Load image
        self.player_win_img = tk.PhotoImage(file=win_player_img)

        # Define label
        player_played_lbl = tk.Label(self, text="You Played: ")
        player_choice_lbl = tk.Label(
            self, textvariable=player_choice)
        comp_played_lbl = tk.Label(self, text="Computer Played: ")
        comp_choice_lbl = tk.Label(
            self, textvariable=computer_choice)
        winner_lbl = tk.Label(
            self, text="You Won!", font=LARGE_FONT)
        player_arm = tk.Label(self, image=self.player_win_img)
        player_score_lbl = tk.Label(self, text="Your score: ")
        player_score_vl = tk.Label(self, textvariable=self.player_score)
        computer_score_lbl = tk.Label(self, text="Computer score: ")
        computer_score_vl = tk.Label(self, textvariable=self.computer_score)

        # Define buttons
        again_btn = tk.Button(
            self, text="Play Again", command=lambda: controller.show_frame(PlayerVsComputer))
        startpage_btn = tk.Button(self, text="Back to start page",
                                  command=lambda: [controller.show_frame(StartPage), self.player_score.set(0), self.computer_score.set(0)])

        # Display
        player_played_lbl.grid(row=0, column=1)
        player_choice_lbl.grid(row=0, column=2)
        comp_played_lbl.grid(row=1, column=1)
        comp_choice_lbl.grid(row=1, column=2)
        winner_lbl.grid(row=2, columnspan=5, pady=10, padx=10)
        player_arm.grid(row=3, columnspan=5, pady=10)
        player_score_lbl.grid(row=4, columnspan=5)
        player_score_vl.grid(row=5, columnspan=5)
        computer_score_lbl.grid(row=6, columnspan=5)
        computer_score_vl.grid(row=7, columnspan=5)
        again_btn.grid(row=8, columnspan=5, pady=10)
        startpage_btn.grid(row=9, columnspan=5)

        self.grid_columnconfigure((0, 4), weight=1)


class Tie(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Access PlayerVsComputer to get variables
        choices = self.controller.access_page(PlayerVsComputer)
        player_choice = choices.player_choice
        computer_choice = choices.computer_choice
        self.player_score = choices.player_score
        self.computer_score = choices.computer_score

        # Load images
        self.computer_win_img = tk.PhotoImage(
            file=win_computer_img).subsample(2, 2)
        self.player_win_img = tk.PhotoImage(file=win_player_img)

        # Define labels
        player_played_lbl = tk.Label(self, text="You Played: ")
        player_choice_lbl = tk.Label(
            self, textvariable=player_choice)
        comp_played_lbl = tk.Label(self, text="Computer Played: ")
        comp_choice_lbl = tk.Label(
            self, textvariable=computer_choice)
        winner_lbl = tk.Label(
            self, text="It's a Tie!", font=LARGE_FONT)
        computer_arm = tk.Label(self, image=self.computer_win_img)
        player_arm = tk.Label(self, image=self.player_win_img)
        player_score_lbl = tk.Label(self, text="Your score: ")
        player_score_vl = tk.Label(self, textvariable=self.player_score)
        computer_score_lbl = tk.Label(self, text="Computer score: ")
        computer_score_vl = tk.Label(self, textvariable=self.computer_score)

        # Define buttons
        again_btn = tk.Button(
            self, text="Play Again", command=lambda: controller.show_frame(PlayerVsComputer))
        startpage_btn = tk.Button(self, text="Back to start page",
                                  command=lambda: [controller.show_frame(StartPage), self.player_score.set(0), self.computer_score.set(0)])

        # Display
        player_played_lbl.grid(row=0, column=1)
        player_choice_lbl.grid(row=0, column=2)
        comp_played_lbl.grid(row=1, column=1)
        comp_choice_lbl.grid(row=1, column=2)
        winner_lbl.grid(row=2, columnspan=5, pady=10)
        computer_arm.grid(row=3, column=1, pady=10, padx=40)
        player_arm.grid(row=3, column=2, pady=10, padx=40)
        player_score_lbl.grid(row=4, columnspan=5)
        player_score_vl.grid(row=5, columnspan=5)
        computer_score_lbl.grid(row=6, columnspan=5)
        computer_score_vl.grid(row=7, columnspan=5)
        again_btn.grid(row=8, columnspan=5, pady=10)
        startpage_btn.grid(row=9, columnspan=5)

        self.grid_columnconfigure((0, 4), weight=1)


class ComputerVsComputer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        game = Game()

        # Access StartPage to get variables
        choices = self.controller.access_page(StartPage)
        result = choices.result
        computer1_choice = choices.computer1_choice
        computer2_choice = choices.computer2_choice
        computer1_score = choices.computer1_score
        computer2_score = choices.computer2_score

        # Load image
        self.computer_img = tk.PhotoImage(file=computer_img)

        # Define labels
        title = tk.Label(
            self, text="Computer VS computer", font=LARGE_FONT)
        match_result_lbl = tk.Label(self, textvar=result, font=LARGE_FONT)
        comp1_played_lbl = tk.Label(self, text="Computer 1 played: ")
        comp1_choice_lbl = tk.Label(self, textvariable=computer1_choice)
        comp2_played_lbl = tk.Label(self, text="Computer 2 played: ")
        comp2_choice_lbl = tk.Label(self, textvariable=computer2_choice)
        comp1_score_lbl = tk.Label(self, text="Computer 1 Score: ")
        comp1_score_vl = tk.Label(self, textvariable=computer1_score)
        comp2_score_lbl = tk.Label(self, text="Computer 2 Score: ")
        comp2_score_vl = tk.Label(self, textvariable=computer2_score)
        winner_img = tk.Label(self, image=self.computer_img)

        # Define buttons
        again_btn = tk.Button(
            self, text="Play Again", command=lambda: [controller.show_frame(ComputerVsComputer), controller.access_page(StartPage).computer_game(game.computer_play)])
        startpage_btn = tk.Button(self, text="Back to start page",
                                  command=lambda: [controller.show_frame(StartPage), computer1_score.set(0), computer2_score.set(0)])

        # Display
        title.grid(columnspan=5, pady=10, padx=10)
        comp1_played_lbl.grid(row=1, column=1)
        comp1_choice_lbl.grid(row=1, column=2)
        comp2_played_lbl.grid(row=2, column=1)
        comp2_choice_lbl.grid(row=2, column=2)
        match_result_lbl.grid(row=3, columnspan=5, pady=10)
        comp1_score_lbl.grid(row=4, column=1)
        comp1_score_vl.grid(row=4, column=2)
        comp2_score_lbl.grid(row=5, column=1)
        comp2_score_vl.grid(row=5, column=2)
        winner_img.grid(row=8, columnspan=5)
        again_btn.grid(row=6, columnspan=5, pady=10)
        startpage_btn.grid(row=7, columnspan=5)

        self.grid_columnconfigure((0, 4), weight=1)


if __name__ == "__main__":
    app = RockPaperScissors()
    app.mainloop()
