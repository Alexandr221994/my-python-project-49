#!/usr/bin/env python3
from brain_games.game_starter import run_game
from brain_games import arg_parser


def main():
    run_game(arg_parser.args_parser())


if __name__ == '__main__':
    main()
