import pytest
import itertools
from RockPaperScissors import Game

game = Game()
choices = game.choices


@pytest.mark.parametrize("command", ["rock", "paper", "scissors"])
def test_player_input(command):
    player = game.player_input(command)
    assert player in choices


def test_computer_input():
    computer = game.computer_input()
    assert computer in choices


@pytest.mark.parametrize("player_choice, computer_choice", [i for i in itertools.product(choices, repeat=2)])
def test_compare_choices(player_choice, computer_choice):
    match = game.compare_choices(player_choice, computer_choice)
    player_score = game.player_score
    computer_score = game.computer_score
    assert match in ["tie", "computerwin", "playerwin"]
    if match == "playerwin":
        assert game.player_score == player_score
        assert game.computer_score == computer_score
    elif match == "computerwin":
        assert game.player_score == player_score
        assert game.computer_score == computer_score
    else:
        assert game.player_score == player_score
        assert game.computer_score == computer_score
