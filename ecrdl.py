"""
CLI utility to download radar images from Environment Canada
"""
from tracklocal import checklocal 

import pandas as pd
import re
from io import BytesIO
from pathlib import Path

from PIL import Image, UnidentifiedImageError
import click 
import httpx


PWD = Path(__file__).parent.resolve()
GIFDIR = PWD.joinpath('gifs')

def dates10m(sdate,edate):
    dt = pd.date_range(sdate,edate, freq='10min')
    return dt

def fullurl(URL, params):
    return URL+'?'+'&'.join([f'{k}={v}' for k,v in params.items()])

def parser(URL):
    return "".join([c for c in str(URL) if re.match(r'\w', c)])

def saveimg(year, month, day, hour, minute):
    time = f'{year:02d}{month:02d}{day:02d}{hour:02d}{minute:02d}'
    params = {'time':time, 'site':'CASKR', 'image_type':'PRECIPET_RAIN_WEATHEROFFICE'}
    URL = "https://climate.weather.gc.ca/radar/image_e.html"
    furl= fullurl(URL, params)
    print(f'attempting to dl {furl}')
    if checklocal(furl, parser):
        print('---skipping, exists---')
        return
    GIFDIR.mkdir(exist_ok=True)
    fp = GIFDIR.joinpath(fn)
    with open(fp, 'wb') as f:
        try:
            r = httpx.get(URL, params=params)
            fn = parser(furl)
            im = Image.open(BytesIO(r.content))
            im.save(f , 'GIF')
        except (UnidentifiedImageError, httpx.ReadTimeout):
            try:
                subprocess.run(["wget", furl], capture_output=True)
            except:
                print('=====skipping, FAILED=====')
        except:
            print('=====skipping, FAILED=====')

@click.command()
@click.option('--sdate', help='start date')
@click.option('--edate', help='end date')
def main(sdate, edate):
    for d in dates10m(sdate, edate):
        saveimg(d.year, d.month, d.day, d.hour, d.minute)

if __name__=='__main__':
    main()
