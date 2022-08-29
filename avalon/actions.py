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

        intent = "examine" if match.groups()[0] == "x" else match.groups()[0]
        if g_object:
            final_desc = g_object.final_description()

            if final_desc == "":
                print(f"'{g_object_name}' doesn't seem to be something you can {intent}.")
            else:
                print(g_object.final_description())
        else:
            print(f"'{g_object_name}' doesn't seem to be something you can {intent}.")


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


class AgainAction(Action):
    def __init__(self):
        super().__init__(r"^again")

    def execute(self, context):
        l_action, l_cmd = context.commands_executed[-2]
        context.cmd = l_cmd
        l_action.execute(context)


all_actions = [LookAction, LookAtAction, JumpAction, AttackAction, AgainAction]
