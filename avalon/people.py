from avalon.objects import GameObject


class Person(GameObject): # Wow, so objectifying
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name

        self.inventory = []

    def description(self):
        return "Same old, same old."