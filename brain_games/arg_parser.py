import argparse
from brain_games.games import calc_game, even_game, gcd_game, prime_game, progression_game

GAMES = {
    'calc': calc_game,
    'even': even_game,
    'gcd': gcd_game,
    'prime': prime_game,
    'progression': progression_game
}


def args_parser(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-gn", "--gamename",
                        help="by adding a certain argument (calc, even, gcd, "
                             "progression, prime) you get a selected game")
    args = parser.parse_args(argv)
    return GAMES[args.gamename]

