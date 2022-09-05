.. Avalon documentation master file, created by
   sphinx-quickstart on Wed Aug 31 15:10:00 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Avalon Docs
==================================
.. toctree::
   Quickstart
   ClassReferences
   Extendables
   Actions
   :maxdepth: 2


Welcome to Avalon! Avalon is a pure Python text adventure development library. It's built on the idea that rebuilding
the wheel with DS languages isn't required. Any game you make with this library, along with the library itself, is built
entirely with Python.

====================
The Basic Game Model
====================

------
Games
------
A **game** in Avalon does not refer to your text adventure as a whole, but rather to a class inheriting from the
``TextAdventure`` class. This class contains all the meta- and non-meta- data for your game, as well as the core methods to
let it run.

----------------
Playing the Game
----------------
Right now, **Avalon does not export to ZCode or to TADS** (Heck, it doesn't even export, technically). This may be implemented in the future, but for now it runs within
its own environment.

-------------------------------------------------
Grammar Rules and Stuff and How They Don't Apply
-------------------------------------------------
~~~~~~~
Actions
~~~~~~~
Everything you do while playing the game is an action. In this way, it borrows from TADS 3. But it does this
by using **regular expressions** or **regex**. **When a player enters a command, it has to match an action's
regex syntax.**

For example, an action called DanceAction could use the expression "^dance to (\s+) music".
Then, when a player enters "dance to hip-hop lo-fi music" (why?) it'll match to ``DanceAction``.

