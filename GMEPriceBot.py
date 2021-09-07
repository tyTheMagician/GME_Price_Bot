# authors - @magician_ty +
import csv
import requests
from datetime import date
from Twitter_API_Info import T_API_KEY, T_KEY_SECRET, T_BEARER_TOKEN
from AlphaVantage_API_Info import AV_API


# TODO:
# get API data from each time-zone where GME is traded
# write-tweet logic
# review
# finalize & test
# go-live

print("GME Price (bot)")
print('-------------------')
print('$GME:')

# Twitter API
# get your API --> https://developer.twitter.com/
# I moved all my API codes into a local py file and plug variables to use them, due to security
TWITTER_API_KEY = T_API_KEY
TWITTER_KEY_SECRET = T_KEY_SECRET
TWITTER_BEARER_TOKEN = T_BEARER_TOKEN

# AlphaVantage API - used for real-time-data in United States
# get your API --> https://www.alphavantage.co/support/#api-key
AV_API_KEY = AV_API

# Date setup
today = date.today()
wD = date.weekday(today)
day = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
    }

# AlphaVantage query - edit the FUNCTION to change the query (time series, symbol, interval)
FUNCTION = 'TIME_SERIES_DAILY&symbol=GME&interval=5min&apikey='
url = 'https://www.alphavantage.co/query?function='+ FUNCTION + AV_API_KEY
r = requests.get(url)
data = r.json()
recentPriceData = data.get('Time Series (Daily)')
now = recentPriceData.get(today)

# Print statements and logic for the Tweets
if day[wD] == 'Saturday' or 'Sunday':
    print('weekend snoozes...')
else:
    print('Today is ' + day[wD])
    print('Price: ' + now['1. open'], '\nVolume: ' + now['5. volume'] + ' / shares traded')
