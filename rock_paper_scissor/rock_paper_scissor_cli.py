import random


class Game:
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

    def player_input(self):
        self.player = input(
            "What will you play? Rock, paper or scissors? \n").lower()
        if self.player not in self.choices:
            print("Input not valid! Please type rock or paper or scissors")
            self.player_input()
        return self.player

    def computer_choice(self):
        self.computer = random.choice(self.choices)
        return self.computer

    def compare_choices(self, player_choice, computer_choice):
        game = []
        game.extend([player_choice, computer_choice])
        if len(set(game)) == 1:
            print("Tie!")
        elif game in self.victory:
            self.player_score += 1
            print(
                f"You played {self.player} and computer played {self.computer}. You win! Your score: {self.player_score}. Computer score: {self.computer_score}")
        else:
            self.computer_score += 1
            print(
                f"You played {self.player} and computer played {self.computer}. Computer wins! Your score: {self.player_score}. Computer score: {self.computer_score}")

    def play_again(self):
        again = input("Do you want to play again? Yes or no? \n").lower()
        if again == 'yes':
            self.play()
        else:
            return

    def play(self):
        game_mode = input(
            "Do you want to play or do you want to watch the computer play against himself?").lower()
        if game_mode == 'me':
            player = self.player_input()
            computer = self.computer_choice()
            self.compare_choices(player, computer)
            self.play_again()
        else:
            player = self.computer_choice()
            computer = self.computer_choice()
            self.compare_choices(player, computer)
            self.play_again()


rps = Game()
rps.play()
