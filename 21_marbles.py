#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Floyd Hightower <https://github.com/fhightower>
# October 2016
"""21 Marble game."""

import argparse

import inflect

AI_NAME = "Marbles_AI"


def init_parser():
    """Initialize the argument parser."""
    parser = argparse.ArgumentParser(description='Play 21 Marble game.')
    parser.add_argument('-a', '--ai', action="store_true", default=False,
                        help="if you want to play against an AI")
    parser.add_argument('player1', type=str, nargs='?', default="player1",
                        help='name of first player (default is "player1")')
    parser.add_argument('player2', type=str, nargs='?', default="player2",
                        help='name of second player (default is "player2")')
    parser.add_argument('marbles', type=int, nargs='?', default=21,
                        help='number of marbles in the game (default is 21)')

    return parser.parse_args()


def get_player_move(marble_count):
    """Get a player's move."""
    while True:
        # get desired move
        desired_move = input("How many marbles would you like to take? ")

        try:  # make sure the desired move is an integer
            desired_move = int(desired_move)
        except ValueError:
            print("! Please enter 1, 2, or 3.")
        else:
            # make sure the desired move is 1, 2, or 3
            if (0 < desired_move < 4):
                # make sure enough marbles to perform the desired move
                if marble_count - desired_move < 0:
                    print("There are only {} marbles ".format(marble_count) +
                          "remaining so you cannot take " +
                          "{} marbles.".format(desired_move))
                else:
                    return desired_move
            else:
                print("! Please enter a number between 1 and 3.")


def main():
    """Start the 21 marble game."""
    args = init_parser()
    inflector = inflect.engine()

    MARBLE_COUNT = args.marbles
    AI = args.ai

    # make sure none of the player names are the same as the AI_NAME
    if args.player1 == AI_NAME:
        print("Sorry, but the name {} cannot be used.  ".format(AI_NAME) +
              "For this game, your name will be: 'player1'")
        args.player1 = "player1"
    elif args.player2 == AI_NAME:
        print("Sorry, but the name {} cannot be used.  ".format(AI_NAME) +
              "For this game, your name will be: 'player2'")
        args.player2 = "player2"

    if AI:  # if there is an AI...
        # set player2 as an AI
        args.player2 = AI_NAME

    turn = args.player1
    move = 0

    while MARBLE_COUNT > 1:
        print("\n{}'s turn...".format(turn.upper()))

        # print the number of marbles remaining
        print("{} ".format(MARBLE_COUNT) +
              "{} remaining".format(inflector.plural("marble", MARBLE_COUNT)))

        if AI and turn == AI_NAME:  # if it is the AI's turn...
            # AI magic :)
            move = 4 - move
            print("I'm taking: {}".format(move))
        else:  # if it is a human's turn...
            # get the human's move
            move = get_player_move(MARBLE_COUNT)

        MARBLE_COUNT -= move

        # switch the turn to the other player
        if turn == args.player1:
            turn = args.player2
        elif turn == args.player2:
            turn = args.player1

    print("\n{} ".format(MARBLE_COUNT) +
          "{} remaining.\n".format(inflector.plural("marble", MARBLE_COUNT)))

    # determine the appropriate winner
    if MARBLE_COUNT == 1:
        if turn == args.player1:
            print("Sorry {}, but there is only one ".format(args.player1) +
                  "marble left and you will have to take it.\nThis means " +
                  "{} is the WINNER.".format(args.player2.upper()))
        else:
            print("Sorry {}, but there is only one ".format(args.player2) +
                  "marble left and you will have to take it.\nThis means " +
                  "{} is the WINNER.".format(args.player1.upper()))
    else:
        if turn == args.player1:
            print("Sorry {}, ".format(args.player2) +
                  "but you took the last marble.\nThis means " +
                  "{} is the WINNER.".format(args.player1.upper()))
        else:
            print("Sorry {}, ".format(args.player1) +
                  "but you took the last marble.\nThis means " +
                  "{} is the WINNER.".format(args.player2.upper()))


if __name__ == '__main__':
    main()
