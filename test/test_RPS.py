import pytest
from src.RPS_piedra_papel_tijeras import Game, GameResult, GameAction


@pytest.fixture
def game():
    '''
    Setup del objeto game
    '''
    setup_game = Game()
    return setup_game


@pytest.mark.draw
def test_draw():


    assert GameResult.Tie == Game.assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Rock)

    assert GameResult.Tie == Game.assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Scissors)

    assert GameResult.Tie == Game.assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Paper)
