from avalon import TextAdventure


def run_game(game: TextAdventure):
    """
    Run the game. Currently, a wrapper for `game.run`, could spin off other functions in the future.

    :param game: The game to run.
    :return:
    """
    game.run()
