class Room:
    def __init__(self, name: str):
        """
        Base class for a room. You should create a subclass of Room and use that in your game, ideally.
        """
        self.name = name
        self.description_string = None

    def description(self, desc=None):
        if not desc:
            return self.description_string
