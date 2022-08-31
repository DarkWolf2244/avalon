import avalon.objects as objects
from typing import List


class Room:
    def __init__(self, name: str):
        """
        Base class for a room. You should create a subclass of Room and use that in your game, ideally.

        :param name: The name of the room to create.
        """
        self.name = name
        self.description_string = None
        self.objects: List[objects.GameObject] = []

    def add_objects(self, *args):
        self.objects.extend(args)

    def description(self, desc=None):
        if not desc:
            return self.description_string

    def final_description(self):
        desc = ""

        desc += self.description()

        for g_object in self.objects:
            inline_desc = g_object.final_inline_description()
            desc += "\n\n" + inline_desc if inline_desc else ""

        return desc
