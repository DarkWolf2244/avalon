from avalon import TextAdventure, Room, run_game


class StudyRoom(Room):
    def __init__(self):
        super().__init__(
            "Study Room"
        )

        self.description_string = "You're standing in a lavish study room. An ornate rosewood desk sits in the " \
                                  "corner, and the only exit seems to be a steel door to the west. "


class TheBookshelf(TextAdventure):
    def __init__(self):
        super().__init__(
            "The Bookshelf",
            "DarkWolf"
        )

        self.set_initial_room(StudyRoom())


game = TheBookshelf()
run_game(game)
