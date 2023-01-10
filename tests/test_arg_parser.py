from brain_games.arg_parser import args_parser
from brain_games.games import calc_game


def test_args_parser(capsys):
    result = args_parser(["--gamename", "calc"])
    assert result == calc_game
