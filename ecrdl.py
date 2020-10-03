"""
CLI utility to download radar images from Environment Canada
"""
import pandas as pd
import re
from io import BytesIO
from pathlib import Path

from PIL import Image
import click 
import httpx

PWD = Path(__file__).parent.resolve()
GIFDIR = PWD.joinpath('gifs')

def dates10m(sdate,edate):
    dt = pd.date_range(sdate,edate, freq='10min')
    return dt

def saveimg(year, month, day, hour, minute):
    time = f'{year:02d}{month:02d}{day:02d}{hour:02d}{minute:02d}'
    params = {'time':time, 'site':'CASKR', 'image_type':'PRECIPET_RAIN_WEATHEROFFICE'}
    URL = "https://climate.weather.gc.ca/radar/image_e.html"
    r = httpx.get(URL, params=params)
    print(f'attempting to dl {r.url}')
    if r.is_error:
        print('=====FAILED=====')
        return 
    #with open(str(r.url), 'w') as f:
    fn ="".join([c for c in str(r.url) if re.match(r'\w', c)])
    GIFDIR.mkdir(exist_ok=True)
    fp = GIFDIR.joinpath(fn)
    with open(fp, 'wb') as f:
        im = Image.open(BytesIO(r.content))
        im.save(f , 'GIF')

#@click.option('--res', type=click.Choice(['10'], case_sensitive=False))
#@click.option('--loc', type=click.Choice(['ON'], case_sensitive=False))

@click.command()
@click.option('--sdate', help='start date')
@click.option('--edate', help='end date')
def main(sdate, edate):
    for d in dates10m(sdate, edate):
        saveimg(d.year, d.month, d.day, d.hour, d.minute)

if __name__=='__main__':
    main()
