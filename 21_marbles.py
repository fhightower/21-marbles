#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Floyd Hightower <https://github.com/fhightower>
# October 2016
"""21 Marbles game."""

import argparse
import logging

import inflect


def init_parser():
    """Initialize the argument parser."""
    logging.debug("initializing the argument parser")
    parser = argparse.ArgumentParser(description='Play 21 Marbles game.')
    parser.add_argument('-a', '--ai', action="store_true", default=False,
                        help="if you want to play against an AI")
    parser.add_argument('marbles', type=int, nargs='?', default=21,
                        help='number of marbles in the game (default is 21)')
    parser.add_argument('player1', type=str, nargs='?', default="player1",
                        help='name of first player (default is "player1")')
    parser.add_argument('player2', type=str, nargs='?', default="player2",
                        help='name of second player (default is "player2")')

    return parser.parse_args()


def get_player_move(marble_count):
    """Get a player's move."""
    while True:
        desired_move = input("How many marbles would you like to take? ")

        try:
            desired_move = int(desired_move)
        except ValueError:
            print("! Please enter 1, 2, or 3.")
        else:
            if (desired_move > 0) and (desired_move < 4):
                if marble_count - desired_move < 0:
                    print("There are only {} marbles ".format(marble_count) +
                          "remaining so you cannot take " +
                          "{} marbles.".format(desired_move))
                else:
                    return desired_move
            else:
                print("! Please enter a number between 1 and 3.")


def main():
    """."""
    logging.debug("started the main function")
    args = init_parser()
    inflector = inflect.engine()

    MARBLE_COUNT = args.marbles
    AI = args.ai

    if AI:
        args.player2 = "21 Marbles AI"

    turn = args.player1

    while MARBLE_COUNT > 1:
        if turn == args.player1:
            print("\n{}'s turn...".format(args.player1.upper()))
            turn = args.player2
        elif turn == args.player2:
            print("\n{}'s turn...".format(args.player2.upper()))
            turn = args.player1

        print("{} ".format(MARBLE_COUNT) +
              "{} remaining".format(inflector.plural("marble", MARBLE_COUNT)))

        move = get_player_move(MARBLE_COUNT)

        MARBLE_COUNT -= move

    print("\n{} ".format(MARBLE_COUNT) +
          "{} remaining.\n".format(inflector.plural("marble", MARBLE_COUNT)))

    if MARBLE_COUNT == 1:
        if turn == args.player1:
            print("Sorry {}, but there is only one ".format(args.player1) +
                  "marble left and you will have to take it.\nThat means " +
                  "{} is the winner.".format(args.player2))
        else:
            print("Sorry {}, but there is only one ".format(args.player2) +
                  "marble left and you will have to take it.\nThat means " +
                  "{} is the winner.".format(args.player1))
    else:
        if turn == args.player1:
            print("Sorry {}, ".format(args.player2) +
                  "but you took the last marble.\nThat means " +
                  "{} is the winner.".format(args.player1))
        else:
            print("Sorry {}, ".format(args.player1) +
                  "but you took the last marble.\nThat means " +
                  "{} is the winner.".format(args.player2))


if __name__ == '__main__':
    log_format = '%(asctime)s %(levelname)s: %(message)s'
    logging.basicConfig(level=logging.WARNING, format=log_format)
    main()
