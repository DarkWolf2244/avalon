========
Actions
========

An **action** is simply a class with special methods and properties that can be applied to the in-game world. Every
action has a ``regex`` property and an ``execute`` method.

The ``regex`` property is a regular expression (read up on those) that is meant to apply to the whole command that the player
enters.

The ``execute`` method is called whenever the action is meant to be run. This contains the action's code. Avalon passes a ``context``
argument to it, which is just the game class.

------------------------
Creating Custom Actions
------------------------

To create a new action, simply create a subclass of ``Action`` and give it the required properties. Then pass it to ``avalon.add_action``.

For example:

.. code-block:: python

    from avalon import Action, add_action

    class DanceAction(Action):
        def __init__(self):
            super().__init__(r"^dance$")

        def execute(self):
            print("You dance to lo-fi hip-hop beats for the next few hours.")

    class WhackAction(Action):
        def __init__(self):
            super().__init__(r"^whack (.+)$")

        def execute(self, context):
            match = self.regex.match(context.cmd)

            d_obj_name = match.groups()[0]
            d_obj = context.get_action_by_name(d_obj_name)

            if not d_obj:
                print(f"It doesn't seem like {d_obj_name} even exists, bud.")

            print(f"You plant a good whack on the {d_obj.the_name}.")

    add_action(DanceAction)
    add_action(WhackAction)

Now, entering ``whack the table`` (if there's a table) will return

.. code-block::

    You plant a good whack on the table.

----------------
List of Actions
----------------

.. autoclass:: avalon.LookAction
.. autoclass:: avalon.LookAtAction
.. autoclass:: avalon.JumpAction
.. autoclass:: avalon.AttackAction
.. autoclass:: avalon.AgainAction
.. autoclass:: avalon.ReadAction
.. autoclass:: avalon.PutOnAction
.. autoclass:: avalon.TakeAction