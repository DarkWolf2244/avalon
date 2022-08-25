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
        super().__init__(r"^(look|l)((?!at).)*$")

    def execute(self, context):
        print(context.current_room.final_description())
        return True


class LookAtAction(Action):
    def __init__(self):
        super().__init__(r"^(look at|examine|x|check) (.+)")

    def execute(self, context):
        match = self.regex.match(context.cmd)
        g_object_name = match.groups()[1]
        g_object = context.get_object_by_name(g_object_name)

        print(g_object.description())


class JumpAction(Action):
    def __init__(self):
        super().__init__(r"^jump")

    def execute(self, ctx):
        print("You jump, like a little child. How fun.")
        return True


class AttackAction(Action):
    def __init__(self):
        super().__init__(r"(fight|attack|kill) (.+)")

    def execute(self, context):
        match = self.regex.match(context.cmd)
        g_object_name = match.groups()[1]
        g_object = context.get_object_by_name(g_object_name)

        if hasattr(g_object, "OnAction_Attack"):
            g_object.OnAction_Attack(context)

        elif g_object_name in ["me", "self", "myself"]:
            print("Why don't you seek some self-harm therapists?")
        elif g_object is None:
            print(f"I don't think '{g_object_name}' is something that you can attack.")

        else:
            print("Tantrums solve nothing.")


all_actions = [LookAction, LookAtAction, JumpAction, AttackAction]
