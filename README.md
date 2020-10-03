# Env Canada Radar Download

CLI utility to download Environment Canada Radar data

Async/threading intentionally left out

## Setup

create virtual env and install requirments
~~~
python3 -m venv venv
source venv/bin/activate 
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
~~~

## Quickstart 

specify start and end dates
~~~
python ecrdl.py --sdate '2020-01-01' --edate '2020-01-01' > ecrdl.log 2>error_ecrdl.log &
~~~

## Requirements
 - Python3.8+
