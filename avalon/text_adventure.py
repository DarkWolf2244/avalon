class TextAdventure:
    def __init__(self, game_name: str, author_name: str, game_description: str = None):
        """
        Create a new text adventure. Ideally, you would create a subclass of this, and pass that to `avalon.run`.

        :param game_name: The name of the text adventure. (E.g.  "The Bookshelf")
        :param author_name: The author of the game, probably you. (E.g. "Andrew Plotkin")
        :param game_description: Optional. The description of the game.
        """

        self.game_name = game_name
        self.author_name = author_name
        self.game_description = None
