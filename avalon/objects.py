class GameObject:
    def __init__(self, name: str):
        self.name = name
        self.description_string = None
        self.inline_description_string = None

    def description(self):
        return self.description_string

    def inline_description(self):
        return self.inline_description_string
