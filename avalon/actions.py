import re


class Action:
    def __init__(self, regex: str):
        """
        Base Action class. Everything inheriting from it is an action.
        """
        self.regex = re.compile(regex)

    def validate(self, cmd: str):
        if self.regex.match(cmd):
            return True
        return False


class LookAction(Action):
    def __init__(self):
        super().__init__(r"^(look|l)")

    def execute(self, context):
        print(context.current_room.description())
        return True


class JumpAction(Action):
    def __init__(self):
        super().__init__(r"^jump")

    def execute(self, ctx):
        print("You jump, like a little child. How fun.")
        return True


all_actions = [LookAction, JumpAction]
