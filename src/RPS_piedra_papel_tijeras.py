import random
from enum import IntEnum


class GameAction(IntEnum):

    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class GameResult(IntEnum):
    VICTORY = 0
    DEFEAT = 1
    TIE = 2


Victories = {
    GameAction.ROCK: GameAction.PAPER,
    GameAction.PAPER: GameAction.SCISSORS,
    GameAction.SCISSORS: GameAction.ROCK
}

class Game:

    def assess_game(user_action, computer_action):

        game_result = None

        if user_action == computer_action:
            print(f"User and computer picked {user_action.name}. Draw game!")
            game_result = GameResult.TIE

        # You picked ROCK
        elif user_action == GameAction.ROCK:
            if computer_action == GameAction.SCISSORS:
                print("ROCK smashes SCISSORS. You won!")
                game_result = GameResult.VICTORY
            else:
                print("PAPER covers ROCK. You lost!")
                game_result = GameResult.DEFEAT

        # You picked PAPER
        elif user_action == GameAction.PAPER:
            if computer_action == GameAction.ROCK:
                print("PAPER covers ROCK. You won!")
                game_result = GameResult.VICTORY
            else:
                print("SCISSORS cuts PAPER. You lost!")
                game_result = GameResult.DEFEAT

        # You picked SCISSORS
        elif user_action == GameAction.SCISSORS:
            if computer_action == GameAction.ROCK:
                print("ROCK smashes SCISSORS. You lost!")
                game_result = GameResult.DEFEAT
            else:
                print("SCISSORS cuts PAPER. You won!")
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