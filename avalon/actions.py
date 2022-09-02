import re
from avalon.extendables import Readable, Surface


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
    """
    Look around the room.

    Regex: ``^(look|l)((?!at).)*$``
    """

    def __init__(self):
        super().__init__(r"^(look|l)((?!at).)*$")

    def execute(self, context):
        print(context.current_room.final_description())
        return True


class LookAtAction(Action):
    """
    Examine or look at an object. Displays its description.

    Regex: ``(look at|examine|x|check) (.+)``
    """
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
    """
    Standard jumping procedure. Does nothing except display a message.

    Regex: ``jump``
    """
    def __init__(self):
        super().__init__(r"^jump")

    def execute(self, ctx):
        print("You jump, like a little child. How fun.")
        return True


class AttackAction(Action):
    """
    Attack or fight something/

    Regex: ``(fight|attack|kill) (.+)``
    """
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
    """
    Repeat the last action.

    Regex: ``^again``
    """
    def __init__(self):
        super().__init__(r"^again")

    def execute(self, context):
        l_action, l_cmd = context.commands_executed[-2]
        context.cmd = l_cmd
        l_action.execute(context)


class ReadAction(Action):
    """
    Read an object. Only applies to objects with a Readable extendable.

    Regex: ``^read (.+)``
    """
    def __init__(self):
        super().__init__(r"^read (.+)")

    def execute(self, context):
        match = self.regex.match(context.cmd)
        g_object_name = match.groups()[0]
        g_object = context.get_object_by_name(g_object_name)

        if not g_object:
            print(f"'{g_object_name} doesn't seem to exist.")
            return

        if g_object.is_of_type(Readable):
            if g_object.readable.content():
                print(g_object.readable.content())
            else:
                # TODO: Raise a game error, because you can't have a readable not have content
                print("")
        else:
            print(f"You can't read the {g_object.the_name}.")


class PutOnAction(Action):
    """
    Put an object on another object. Only applies if the indirect object has a Surface extendable.

    Regex: ``^(put|place) (.+) (on|on top of|upon) (.+)$``
    """
    def __init__(self):
        super().__init__(r"^(put|place) (.+) (on|on top of|upon) (.+)$")

    def execute(self, context):
        match = self.regex.match(context.cmd)

        intent_1, d_obj_name, intent_2, i_obj_name = match.groups()

        d_obj = context.get_object_by_name(d_obj_name)
        i_obj = context.get_object_by_name(i_obj_name)

        if not d_obj or not i_obj:
            unknown = d_obj_name if not d_obj else i_obj_name

            print(f"'{unknown} doesn't seem to exist.")

            return

        if not i_obj.is_of_type(Surface):
            print(f"You can't put things on the {i_obj.the_name}.")

            return

        i_obj.parent.objects.remove(i_obj)

        d_obj.add_object(i_obj)

        print(f"You {intent_1} the {d_obj_name} {intent_2} the {i_obj_name}.")


class TakeAction(Action):
    """
    WIP.
    """
    def __init__(self):
        super().__init__(r"^(take|get) (.+)")

    def execute(self, context):
        match = self.regex.match(context.cmd)
        intent, d_obj_name = match.groups()

        d_obj = context.get_object_by_name(d_obj_name)

        if not d_obj:
            print(f"'{d_obj_name} doesn't seem to exist.")

        d_obj.parent.objects.remove(d_obj)

        d_obj.parent = context.player
        context.player.inventory.append(d_obj)

        print(f"You {intent} the {d_obj_name}.")


all_actions = [LookAction, LookAtAction, JumpAction, AttackAction, AgainAction, ReadAction, PutOnAction, TakeAction]


def add_action(action):
    all_actions.append(action)
