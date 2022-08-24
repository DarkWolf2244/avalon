from avalon import TextAdventure, Room, run_game


class StudyRoom(Room):
    def __init__(self):
        super().__init__(
            "Study Room"
        )

        self.desc_counter = 0

    def description(self, desc=None):
        all_descs = [
            "You're standing in a lavish study room. An ornate rosewood desk sits in the corner, and the only exit "
            "seems to be a steel door to the west.",
            "This is a study room. An ornate desk is in the corner, and there's a steel door to the west."
        ]

        if self.desc_counter == 1:
            self.desc_counter = 0
        else:
            self.desc_counter = 1
            
        return all_descs[self.desc_counter]



class TheBookshelf(TextAdventure):
    def __init__(self):
        super().__init__(
            "The Bookshelf",
            "DarkWolf"
        )

        self.set_initial_room(StudyRoom())


game = TheBookshelf()
run_game(game)
