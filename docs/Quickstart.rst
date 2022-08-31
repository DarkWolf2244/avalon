====================
Quickstart
====================

Get, set, go. Create a new Python script, and import ``TextAdventure``, ``Room`` and ``run_game``.

.. code-block:: python

    from avalon import TextAdventure, Room, run_game


Now, to create a text adventure, simply create a class inheriting from ``TextAdventure``.

.. code-block:: python

    class IntroGame(TextAdventure):
        pass

Within it, invoke the ``super().__init__`` with the arguments needed to create the game.

.. code-block:: python

    class IntroGame(TextAdventure):
        super().__init__("Intro Game", "FixYourPosture")

Here's all the args:

.. autofunction:: avalon.TextAdventure.__init__
    :noindex:

Once you're done with that, you need to create a new room to start in. This room is called the **inital room**.

Create a new class inheriting from ``Room``. Just like for the game itself, call ``super().__init__`` with the required
args.

.. code-block:: python

    class IntroRoom(Room):
        super().__init__("Initial Room")


Here are the args for the ``Room`` class:

.. autofunction:: avalon.Room.__init__
    :noindex:

All rooms have a *description*. That's what displayed when they enter it or type ``look``. It's just a string, but Python
doesn't have dynamically-generated strings. We work around that by making these sorts of strings *methods* rather than
just variables. But for simplicity, we *also* allow strings as variables.

For example, the description for ``IntroRoom`` could be stored like this:

.. code-block:: python

    class IntroRoom(Room):
        def __init__(self):
            super().__init__("Initial Room")

            self.description_string = "This is the initial room. Not much to see here."


... or like this:

.. code-block:: python

    class IntroRoom(Room):
        def __init__(self):
            super().__init__("Initial Room")

        def description(self):
            return "This is the initial room. Not much to see here."


The beauty of this is that now the description can vary on demand. You can change the description based on whether the player
ate a doughnut, read a book or stuffed a body in the trunk of a car (no, seriously, that's a classic plot line).

