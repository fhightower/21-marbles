# 21 Marbles

The code in this repo. is inspired by a game which involves 21 marbles.  The rules of the game are simple:

- There are 21 marbles (or other objects) in a central set.
- Two players take turns removing 1, 2, or 3 marbles from the central set.
- A player **must** remove at least one marble when it is his/her turn.
- The player who takes the last marble loses (or it can be played such that the player who takes the last marble wins).

I like to use this game to teach some basic principles of game theory.  It is a very simple game that has some fun and often surprising results when one starts to investigate it.

## Usage
```
usage: 21_marbles.py [-h] [-a] [player1] [player2] [marbles]

Play 21 Marble game.

positional arguments:
  player1     name of first player (default is "player1")
  player2     name of second player (default is "player2")
  marbles     number of marbles in the game (default is 21)

optional arguments:
  -h, --help  show this help message and exit
  -a, --ai    if you want to play against an AI
```
