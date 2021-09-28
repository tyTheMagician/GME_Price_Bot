# authors - @magician_ty
# GME Price Bot - Tweeting $GME price and volume, every 30 minutes in markets where $GME is traded


import os
from time import time, localtime, strftime, sleep
import pandas as pd
import tweepy
from datetime import datetime, date, timedelta
from Twitter_API_Info import Consumer_Key, Consumer_Secret, Access_Token, Access_Secret
from twelvedata import TDClient
from TwelveData_API import US_STOCK_API


print("""
    ###################
    ## GME Price Bot ##
    ###################
    """)

# Tweet Tweet
def tweet(message):
    auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
    auth.set_access_token(Access_Token, Access_Secret)
    api = tweepy.API(auth)
    api.update_status(message)


# Get price + volume
def getStockData(time):
    td = TDClient(apikey=US_STOCK_API)
    ts = td.time_series(
        symbol="GME",
        interval="5min",
        start_date=time,
        outputsize=3000,
        order='ASC'
    ).as_pandas()

    price = '{:.2f}'.format(ts.iloc[0, 0])
    priceClose = '{:.2f}'.format(ts.iloc[0, 3])
    volumeTraded = ts['volume'].sum()
    volume = '{:,}'.format(volumeTraded)

    return price, volume, priceClose


def timeLeft(target, now):
    targetTime = target - now
    secondsLeft = targetTime.total_seconds()

    return secondsLeft

# Main loop
while True:

    # Date setup
    today = date.today()
    now = datetime.now().replace(microsecond=0, second=0)
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

    # Time-slot variables
    today930 = pd.to_datetime(str(today) + ' 09:30:00')
    today10 = pd.to_datetime(str(today) + ' 10:00:00')
    today1030 = pd.to_datetime(str(today) + ' 10:30:00')
    today11 = pd.to_datetime(str(today) + ' 11:00:00')
    today1130 = pd.to_datetime(str(today) + ' 11:30:00')
    today12 = pd.to_datetime(str(today) + ' 12:00:00')
    today1230 = pd.to_datetime(str(today) + ' 12:30:00')
    today13 = pd.to_datetime(str(today) + ' 13:00:00')
    today1330 = pd.to_datetime(str(today) + ' 13:30:00')
    today14 = pd.to_datetime(str(today) + ' 14:00:00')
    today1430 = pd.to_datetime(str(today) + ' 14:30:00')
    today15 = pd.to_datetime(str(today) + ' 15:00:00')
    today1530 = pd.to_datetime(str(today) + ' 15:30:00')
    today1555 = pd.to_datetime(str(today) + ' 15:55:00')
    today16 = pd.to_datetime(str(today) + ' 16:00:00')
    today1630 = pd.to_datetime(str(today) + ' 16:30:00')
    todayEnd = pd.to_datetime(str(today) + ' 23:59:59')
    marketOpen = today930
    marketClose = today16


    # weekend
    if wD > 4:
        print('[gme bot: weekend | no data | sleeping for ~24 hrs...]')
        sleep(15727)

    # if market is awaiting market open, wait
    elif marketOpen > now:
        timeLeft = marketOpen - now
        secsLeft = timeLeft.total_seconds()
        print('[gme bot: waiting ' + str(secsLeft / 60) + ' minutes for market open...]')
        sleep(secsLeft)

    # if market closed, wait till end of day
    elif today1630 <= now:
        timeLeft = todayEnd - now
        secsLeft = timeLeft.total_seconds()
        print('[gme bot: market closed | waiting ' + str(secsLeft / 120) + ' est. hours till EOD')
        sleep(secsLeft)
        sleep(9)

    else:
        ################
        ## 9:30 AM ET ##
        ################

        if today930 <= now:
            if now < today10:
                try:
                    # 9:30 update
                    sleep(60)
                    update930 = '$GME: $' + getStockData(today930)[0] + ' | Volume: ' + getStockData(marketOpen)[1] + ' [shares traded since open]'
                    # 9:30 tweet
                    print('[gme bot: 9:30am]', update930)
                    tweet(update930)
                    print('success')
                    sleep(timeLeft(today10, now))

                except Exception as e:
                    print('[gme bot: 9:30am tweet | data is likely not ready. waiting a minute...]')
                    sleep(60)


        #################
        ## 10:00 AM ET ##
        #################

        if today10 <= now:
            if now < today1030:
                try:
                    # 10:00 update
                    sleep(60)
                    update10 = '$GME: $' + getStockData(today10)[0] + ' | Volume: ' + getStockData(marketOpen)[1] + ' [shares traded since open]'
                    # 10:00 tweet
                    print('[gme bot: 10am]', update10)
                    tweet(update10)
                    print('success')
                    sleep(timeLeft(today1030, now))

                except Exception as e:
                    print('[gme bot: 10am tweet | data is likely not ready. waiting a minute...]')
                    sleep(60)


        #################
        ## 10:30 AM ET ##
        #################

        if today1030 <= now:
            if now < today11:
                try:
                    # 10:30 update
                    sleep(60)
                    update1030 = '$GME: $' + getStockData(today1030)[0] + ' | Volume: ' + getStockData(marketOpen)[1] + ' [shares traded since open]'
                    # 10:30 tweet
                    print('[gme bot: 10:30am]', update1030)
                    tweet(update1030)
                    print('success')
                    sleep(timeLeft(today11, now))

                except Exception as e:
                    print('[gme bot: 10:30am tweet | data is likely not ready. waiting a minute...]')
                    sleep(60)


        #################
        ## 11:00 AM ET ##
        #################

        if today11 <= now:
            if now < today1130:
                try:
                    # 11:00 update
                    sleep(60)
                    update11 = '$GME: $'+ getStockData(today11)[0] + ' | Volume: ' + getStockData(marketOpen)[1] + ' [shares traded since open]'
                    # 11:00 tweet
                    print('[gme bot @ {}'.format(strftime('%H:%M', localtime())), update11)
                    tweet(update11)
                    print('success')
                    sleep(timeLeft(today1130, now))

                except Exception as e:
                    print('[gme bot: 11am tweet | data is likely not ready. waiting a minute...]')
                    sleep(60)


        #################
        ## 11:30 AM ET ##
        #################

        if today1130 <= now:
            if now < today12:
                try:
                    # 11:30 update
                    sleep(60)
                    update1130 = '$GME: $' + getStockData(today1130)[0] + ' | Volume: ' + getStockData(marketOpen)[1] + ' [shares traded since open]'
                    # 11:30 tweet
                    print('[gme bot @ {}'.format(strftime('%H:%M', localtime())), update1130)
                    tweet(update1130)
                    print('success')
                    sleep(timeLeft(today12, now))

                except Exception as e:
                    print('[gme bot: 11:30am tweet | data is likely not ready. waiting a minute...]')
                    sleep(60)


        #################
        ## 12:00 PM ET ##
        #################

        if today12 <= now:
            if now < today1230:
                try:
                    # 12:00 update
                    sleep(60)
                    update12 = '$GME: $' + getStockData(today12)[0] + ' | Volume: ' + getStockData(marketOpen)[1] + ' [shares traded since open]'
                    # 12:00 tweet
                    print('[gme bot: 12pm]', update12)
                    tweet(update12)
                    print('success')
                    sleep(timeLeft(today1230, now))

                except Exception as e:
                    print('[gme bot: 12pm tweet | data is likely not ready. waiting a minute...]')
                    sleep(60)


        #################
        ## 12:30 PM ET ##
        #################

        if today1230 <= now:
            if now < today13:
                try:
                    # 12:30 update
                    sleep(60)
                    update1230 = '$GME: $' + getStockData(today1230)[0] + ' | Volume: ' + getStockData(marketOpen)[1] + ' [shares traded since open]'
                    # 12:30 tweet
                    print('[gme bot: 12:30pm]', update1230)
                    tweet(update1230)
                    print('success')
                    sleep(timeLeft(today13, now))

                except Exception as e:
                    print('[gme bot: 12:30pm tweet | data is likely not ready. waiting a minute...]')
                    sleep(60)


        #################
        ## 1:00 PM ET ##
        #################

        if today13 <= now:
            if now < today1330:
                try:
                    # 1:00 update
                    sleep(60)
                    update13 = '$GME: $' + getStockData(today13)[0] + ' | Volume: ' + getStockData(marketOpen)[1] + ' [shares traded since open]'
                    # 1:00 tweet
                    print('[gme bot: 1pm]', update13)
                    tweet(update13)
                    print('success')
                    sleep(timeLeft(today1330, now))

                except Exception as e:
                    print('[gme bot: 1pm tweet | data is likely not ready. waiting a minute...]')
                    sleep(60)


        #################
        ## 1:30 PM ET ##
        #################

        if today1330 <= now:
            if now < today14:
                try:
                    # 1:30 update
                    sleep(60)
                    update1330 = '$GME: $' + getStockData(today1330)[0] + ' | Volume: ' + getStockData(marketOpen)[1] + ' [shares traded since open]'
                    # 1:30 tweet
                    print('[gme bot: 1:30pm]', update1330)
                    tweet(update1330)
                    print('success')
                    sleep(timeLeft(today14, now))

                except Exception as e:
                    print('[gme bot: 1:30pm tweet | data is likely not ready. waiting a minute...]')
                    sleep(60)


        #################
        ## 2:00 PM ET ##
        #################

        if today14 <= now:
            if now < today1430:
                try:
                    # 2:00 update
                    sleep(60)
                    update14 = '$GME: $' + getStockData(today14)[0] + ' | Volume: ' + getStockData(marketOpen)[1] + ' [shares traded since open]'
                    # 2:00 tweet
                    print('[gme bot: 2pm]', update14)
                    tweet(update14)
                    print('success')
                    sleep(timeLeft(today1430, now))

                except Exception as e:
                    print('[gme bot: 2pm tweet | data is likely not ready. waiting a minute...]')
                    sleep(60)


        #################
        ## 2:30 PM ET ##
        #################

        if today1430 <= now:
            if now < today15:
                try:
                    # 2:30 update
                    sleep(60)
                    update1430 = '$GME: $' + getStockData(today1430)[0] + ' | Volume: ' + getStockData(marketOpen)[1] + ' [shares traded since open]'
                    # 2:30 tweet
                    print('[gme bot: 2:30pm]', update1430)
                    tweet(update1430)
                    print('success')
                    sleep(timeLeft(today15, now))

                except Exception as e:
                    print('[gme bot: 2:30pm tweet | data is likely not ready. waiting a minute...]')
                    sleep(60)


        #################
        ## 3:00 PM ET ##
        #################

        if today15 <= now:
            if now < today1530:
                try:
                    # 3:00 update
                    sleep(60)
                    update15 = '$GME: $' + getStockData(today15)[0] + ' | Volume: ' + getStockData(marketOpen)[1] + ' [shares traded since open]'
                    # 3:00 tweet
                    print('[gme bot: 3pm]', update15)
                    tweet(update15)
                    print('success')
                    sleep(timeLeft(today1530, now))

                except Exception as e:
                    print('[gme bot: 3pm tweet | data is likely not ready. waiting a minute...]')
                    sleep(60)


        #################
        ## 3:30 PM ET ##
        #################

        if today1530 <= now:
            if now < today16:
                try:
                    # 3:30 update
                    sleep(60)
                    update1530 = '$GME: $' + getStockData(today1530)[0] + ' | Volume: ' + getStockData(marketOpen)[1] + ' [shares traded since open]'
                    # 3:30 tweet
                    print('[gme bot: 3:30pm]', update1530)
                    tweet(update1530)
                    print('success')
                    sleep(timeLeft(today16, now))
                    sleep(30)

                except Exception as e:
                    print('[gme bot: 3:30pm tweet | data is likely not ready. waiting a minute...]')
                    sleep(30)


        #################
        ## 4:00 PM ET ##
        #################

        if today16 <= now:
            try:
                # 4:00 update
                sleep(60)
                update16 = '$GME: $' + getStockData(today1555)[2] + ' | Volume: ' + getStockData(marketOpen)[1] + ' [shares traded since open]'
                # 4:00 tweet
                print('[gme bot: 4pm ]', update16)
                tweet(update16)
                print('success')
                sleep(timeLeft(todayEnd, now))

            except Exception as e:
                print('[gme bot: 4pm tweet | data is likely not ready. waiting a minute...]')
                sleep(120)
