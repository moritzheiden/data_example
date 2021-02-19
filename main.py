from functions.helpers import *
from pyalgotrade.bitcoincharts import barfeed
from pyalgotrade.tools import resample
from pyalgotrade import bar
import datetime
import os

# check data files here https://api.bitcoincharts.com/v1/csv/
which_data = 'bitstampUSD.csv.gz'

input_path = 'data/'
if not os.path.exists(input_path):
    os.makedirs(input_path)

start_date = datetime.datetime(2017, 1, 1)
frequency = 60 # aggregate to frequency in minutes
url = f'http://api.bitcoincharts.com/v1/csv/{which_data}'
download_file(url,input_path, which_data)
barFeed = barfeed.CSVTradeFeed()
barFeed.addBarsFromCSV(f'{input_path}{which_data.strip(".gz")}', fromDateTime=start_date)
resample.resample_to_csv(barFeed, bar.Frequency.MINUTE*frequency, f'{input_path }{frequency}min_{which_data.strip(".gz")}')

