import random
from enum import IntEnum


class GameAction(IntEnum):

    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    LIZARD = 3
    SPOCK = 4

class GameResult(IntEnum):
    VICTORY = 0
    DEFEAT = 1
    TIE = 2


victories = {
            GameAction.ROCK:(
                GameAction.SCISSORS, GameAction.LIZARD
            ),
            GameAction.PAPER:(
                GameAction.SPOCK, GameAction.ROCK
            ),
            GameAction.SCISSORS:(
                GameAction.PAPER, GameAction.LIZARD
            ),
            GameAction.SPOCK:(
                GameAction.SCISSORS, GameAction.ROCK
            ),
            GameAction.LIZARD:(
                GameAction.SPOCK, GameAction.PAPER
            ),
        }

class Game:

    def assess_game(user_action, computer_action):

        game_result = None

        if computer_action == user_action:
            print("tie")
            game_result = GameResult.TIE
        elif computer_action in victories[user_action]:
            print("lol you win")
            game_result = GameResult.DEFEAT
        else:
            print("you lost")
            game_result = GameResult.VICTORY

        return game_result


    def get_computer_action():
        computer_selection = random.randint(0, len(GameAction) - 1)
        computer_action = GameAction(computer_selection)
        print(f"Computer picked {computer_action.name}.")

        return computer_action


    def get_user_action():
        # Scalable to more options (beyond ROCK, PAPER and SCISSORS...)
        game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
        game_choices_str = ", ".join(game_choices)
        user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
        user_action = GameAction(user_selection)

        return user_action


    def play_another_round():
        another_round = input("\nAnother round? (y/n): ")
        return another_round.lower() == 'y'


def main():

    while True:
        try:
            user_action = Game.get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = Game.get_computer_action()
        Game.assess_game(user_action, computer_action)

        if not Game.play_another_round():
            break


if __name__ == "__main__":
    main()