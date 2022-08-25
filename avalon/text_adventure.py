import avalon.rooms as rooms
import avalon.actions as actions
import avalon.objects as objects

from rich import print as r_print


class TextAdventure:
    def __init__(self, game_name: str, author_name: str, game_description: str = None):
        """
        Create a new text adventure. Ideally, you would create a subclass of this, and pass that to `avalon.run`.

        :param game_name: The name of the text adventure. (E.g.  "The Bookshelf")
        :param author_name: The author of the game, probably you. (E.g. "Andrew Plotkin")
        :param game_description: Optional. The description of the game.
        """

        self.current_room = None
        self.game_name = game_name
        self.author_name = author_name
        self.game_description = None

        self.initial_room: rooms.Room | None = None

        self.rooms = [self.initial_room]

        self.cmd = ""

    def check_if_game_valid(self):
        if self.initial_room is None:
            r_print(
                "[bold red]ERROR: [/bold red][red]The game does not have an initial room set. Please set the initial "
                "room using [i]game.set_initial_room()[/i].")

            return False

        return True

    def set_initial_room(self, room: rooms.Room):
        self.rooms.remove(self.initial_room)
        self.initial_room = room
        self.rooms.append(self.initial_room)

    def get_object_by_name(self, name: str) -> objects.GameObject:
        for room in self.rooms:
            for g_object in room.objects:
                if g_object.name == name:
                    return g_object

    def run(self):
        if not self.check_if_game_valid():
            print("Exited game execution - please fix any errors displayed above.")
            exit(1)

        r_print(
            f"""[bold cyan]{self.game_name}[/bold cyan]\nBy [bold green]{self.author_name}[/bold green]\n{'-' * len(self.game_name)}"""
        )

        print("")
        r_print(f"[bold cyan]{self.initial_room.name}")

        self.current_room = self.initial_room

        print("")
        print(self.current_room.final_description())

        while True:
            cmd = input("\n> ")

            self.cmd = cmd
            for action in actions.all_actions:
                act = action()

                if act.validate(cmd):
                    act.execute(self)
                    break

            else:
                print(f"I don't understand what you mean by '{cmd}'.")
