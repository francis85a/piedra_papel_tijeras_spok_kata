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


    assert GameResult.TIE == Game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.ROCK)

    assert GameResult.TIE == Game.assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.SCISSORS)

    assert GameResult.TIE == Game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.PAPER)

@pytest.mark.rock
def test_rock_loses():
    '''
    Rock pierde con Spock y Paper 
    '''

    assert GameResult.VICTORY == Game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.ROCK)
    
@pytest.mark.rock
def test_rock_wins():
    '''
    Rock gana a Scissors y Lizard 
    '''
    assert GameResult.DEFEAT == Game.assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.ROCK)
    
@pytest.mark.paper
def test_paper_loses():
    '''
    Paper pierde con Scissors y Lizard 
    '''
    assert GameResult.VICTORY == Game.assess_game(
        user_action=GameAction.SCISSORS,
        computer_action=GameAction.PAPER)

@pytest.mark.paper
def test_paper_wins():
    '''
    Paper gana a Rock y Spock 
    '''
    assert GameResult.DEFEAT == Game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.PAPER)
    
@pytest.mark.scissors
def test_scissors_loses():
    '''
    Scissors pierde con Spock y Rock 
    '''
    assert GameResult.VICTORY == Game.assess_game(
        user_action=GameAction.ROCK,
        computer_action=GameAction.SCISSORS)


@pytest.mark.scissors
def test_scissors_wins():
    '''
    Scissors gana a Lizard y Paper 
    '''
    assert GameResult.DEFEAT == Game.assess_game(
        user_action=GameAction.PAPER,
        computer_action=GameAction.SCISSORS)