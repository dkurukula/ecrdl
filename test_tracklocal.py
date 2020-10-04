import tracklocal
import ecrdl
from pathlib import Path
import re


def test_checklocal():
    #TODO create test dir 
    GIFDIR = Path(__file__).parent.joinpath('gifs')
    URL = 'https://climate.weather.gc.ca/radar/image_e.html?time=202002031240&site=CASKR&image_type=PRECIPET_RAIN_WEATHEROFFICE'
    assert tracklocal.checklocal(URL, ecrdl.parser) == True

