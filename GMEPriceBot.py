# authors - @magician_ty +
import csv
import requests
from datetime import date
import tweepy
import os
import time
from Twitter_API_Info import Consumer_Key, Consumer_Secret, Access_Token, Access_Secret
from AlphaVantage_API_Info import AV_API


# TODO:
# get API data from each time-zone where GME is traded
# write-tweet logic
# review
# finalize & test
# go-live

print("GME Price (bot)")
print('---------------')
print('$GME:')

# Twitter/Tweepy Auth
auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
auth.set_access_token(Access_Token, Access_Secret)
api = tweepy.API(auth)

# AlphaVantage API - used for real-time-data in United States
# get API --> https://www.alphavantage.co/support/#api-key
AV_API_KEY = AV_API

# Date setup 'nameOfDay' holds the value of whatever day it is (mon, tues, wed...)
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

nameOfDay = day[wD]

# AlphaVantage query - edit the FUNCTION to change the query (time series, symbol, interval)
FUNCTION = 'TIME_SERIES_DAILY&symbol=GME&interval=5min&apikey='
url = 'https://www.alphavantage.co/query?function='+ FUNCTION + AV_API_KEY
r = requests.get(url)
data = r.json()
recentPriceData = data.get('Time Series (Daily)')

# ||| delete after testing - needed during off hours, otherwise will return null / 'weekend snoozes...'
today = '2021-09-10'
nameOfDay = 'Friday'
# end of delete |||
now = recentPriceData.get(today)

# formatting text before logic and print statements
p = round(float(now['1. open']), 2)
price = str(p)
volume = int(now['5. volume'])

# Logic and Print statements for the Tweets - better logic needed for holidays and trading hours.
if nameOfDay == 'Saturday':
    print('weekend snoozes...')
elif nameOfDay == 'Sunday':
    print('weekend snoozes...')
else:
    # Opening bell Tweet
    print('Today is ' + day[wD])
    print('Opening Bell - 9:30 AM ET\n')
    print('Price: $' + price + '\nVolume: ' + "{:,}".format(volume) + ' / shares traded since open')
    time.sleep(1)

    # Tweet
    Tweet = api.update_status('test')


    
