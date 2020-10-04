from pathlib import Path

CWD = Path(__file__).parent
GIFDIR = CWD.joinpath('gifs')

def checklocal(fn, parser):
    return GIFDIR.joinpath(parser(fn)).exists()

