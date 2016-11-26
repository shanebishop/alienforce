# alienforce
Python Variation of Robert Epps's 1990s computer game Alienforce

This repository contains source code written in python which emulate a program that was written by Microsoft software developer Robert Epps in C in the 1990s. Epps's original game was written as a personal project, but it was later rewritten and revamped, and then distributed in one of Microsoft's Entertainment Packs for the Windows 9x family of operating systems.

This project was implemented in stages, as evidenced by the different names of the individual .py files.

alienforce1.py generates the graphics only.

alienforce2.py adds the ability to move the ship through the grid, but does not allow the ship to change the direction it is facing or fire shots. The ship can move up, down, left, or right, and is prevented from moving through obstacles in the grid or moving outside the window of play. The ship moves in the last direction it was told to move in until given another command or colliding with an obstacle. The program remembers the last command given by the user, and moves the ship accordingly once the ship can change direction; however, at this stage of implementation, this may be jerky.

alienforce3.py adds the ability for the ship to change direction as it moves around the grid. There is still some jerky movement when changing direction.

alienforce4.py adds the ability of the player to fire shots.

Next steps:
 - Add enemy ships for the player to fight against
 - Develop an AI to control the behaviour of the enemy ships
 - Implement a form of levels that allows play to become progressively more difficult as the player progresses through different levels of play
 - Add additional features to the user interface and additional functionality
 - Add animations and sound effects
 - Add additional functionality to improve gameplay and entertainment
