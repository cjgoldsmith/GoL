# GoL
Game of Life implementation in python

## How to run:
* Clone the GoL repository and navigate to ./GoL
* Run: python main.py

## How to write plugin:

* Import GoL.LifeRule and extend that class
* The class is expected to be callable and must return LifeRule.ALIVE, LifeRule.DEAD or LifeRule.INERT
* The call is made with one positional argument which represents a 3x3 adjacency board with the position in question occupying the center.
  * Return values of ALIVE or DEAD will stop further rules from executing
  * Return value of INERT suggests that this rule does not influence the board.


## Considerations

This is written as an example peice of code because most professional experiences do not provide you the ability to
write code that can be public facing and as of yet I have not had the ability to contribute to an open source community.

It was specifically written to be bare bones and avoids importing library solutions purposefully. I have no doubt there
is a 2x2 grid solution that is better than mine but there is a need to show that I can actually program.

## Future work

Add the ability to import GoL patterns from a file / api / database.
Abstract the idea of the grid away from the GoL class.
Add caching to the rule calls so that repeated calls on the same 3x3 grid require less logic.