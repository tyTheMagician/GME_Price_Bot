# authors - @magician_ty
# GME Price Bot - Tweeting $GME price and volume, every 30 minutes in markets where $GME is traded


import os
import time
import pandas as pd
import tweepy
import logging
from datetime import datetime, date, timedelta
from Twitter_API_Info import Consumer_Key, Consumer_Secret, Access_Token, Access_Secret
from twelvedata import TDClient
from TwelveData_API import US_STOCK_API


print('###################')
print("## GME Price Bot ##")
print('###################')

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
        interval="30min",
        start_date=time,
        outputsize=3000,
        order='ASC'
    ).as_pandas()

    price = '{:.2f}'.format(ts.iloc[0, 0])
    volumeTraded = ts['volume'].sum()
    volume = '{:,}'.format(volumeTraded)

    return price, volume


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
    today4 = pd.to_datetime(str(today) + ' 04:00:00')
    today430 = pd.to_datetime(str(today) + ' 04:30:00')
    today5 = pd.to_datetime(str(today) + ' 05:00:00')
    today530 = pd.to_datetime(str(today) + ' 05:30:00')
    today6 = pd.to_datetime(str(today) + ' 06:00:00')
    today630 = pd.to_datetime(str(today) + ' 06:30:00')
    today7 = pd.to_datetime(str(today) + ' 07:00:00')
    today730 = pd.to_datetime(str(today) + ' 07:30:00')
    today8 = pd.to_datetime(str(today) + ' 08:00:00')
    today830 = pd.to_datetime(str(today) + ' 08:30:00')
    today9 = pd.to_datetime(str(today) + ' 09:00:00')
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
    today16 = pd.to_datetime(str(today) + ' 16:00:00')
    today1630 = pd.to_datetime(str(today) + ' 16:30:00')
    today17 = pd.to_datetime(str(today) + ' 17:00:00')
    today1730 = pd.to_datetime(str(today) + ' 17:30:00')
    today18 = pd.to_datetime(str(today) + ' 18:00:00')
    today1830 = pd.to_datetime(str(today) + ' 18:30:00')
    today19 = pd.to_datetime(str(today) + ' 19:00:00')
    today1930 = pd.to_datetime(str(today) + ' 19:30:00')
    today20 = pd.to_datetime(str(today) + ' 20:00:00')
    preMarket = today4
    marketOpen = today930
    afterMarket = today16
    marketClose = today20

    # weekend
    if wD > 4:
        print('[gme bot: weekend | no data | sleeping for ~24 hrs...]')
        time.sleep(15727)

    # if market is awaiting pre-market, wait
    elif preMarket > now:
        timeLeft = marketOpen - now
        secsLeft = timeLeft.total_seconds()
        print('[gme bot: waiting ' + str(secsLeft * 60) + ' min. for pre-market open...]')
        time.sleep(timeLeft(preMarket, now))

    # if market closed, wait for 17.5 hrs till pre-market
    elif marketClose <= now:
        print('[gme bot: market closed - entering post-market | no data for Ver. 1 | sleeping till morning (17.5 hrs)...]')
        time.sleep(21600)

    else:
        ################
        ## 4:00 AM ET ##
        ################

        if today4 <= now:
            if now < today430:
                try:
                    # 4:00 update
                    update4 = '$GME:' + '\n' + 'Price: $' + getStockData(today4)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 4:00 tweet
                    print('[gme bot: 4am ]', update4)
                    # tweet(update430)
                    time.sleep(timeLeft(today430, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 4am tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        ################
        ## 4:30 AM ET ##
        ################

        if today430 <= now:
            if now < today5:
                try:
                    # 4:30 update
                    update430 = '$GME:' + '\n' + 'Price: $' + getStockData(today430)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 4:30 tweet
                    print('[gme bot: 4:30am ]', update430)
                    # tweet(update430)
                    time.sleep(timeLeft(today5, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 4:30am tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        ################
        ## 5:00 AM ET ##
        ################

        if today5 <= now:
            if now < today530:
                try:
                    # 5:00 update
                    update5 = '$GME:' + '\n' + 'Price: $' + getStockData(today5)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 5:00 tweet
                    print('[gme bot: 5am ]', update5)
                    # tweet(update5)
                    time.sleep(timeLeft(today530, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 5am tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        ################
        ## 5:30 AM ET ##
        ################

        if today530 <= now:
            if now < today6:
                try:
                    # 5:30 update
                    update530 = '$GME:' + '\n' + 'Price: $' + getStockData(today530)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 5:30 tweet
                    print('[gme bot: 5:30am ]', update530)
                    # tweet(update530)
                    time.sleep(timeLeft(today6, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 5:30am tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        ################
        ## 6:00 AM ET ##
        ################

        if today6 <= now:
            if now < today630:
                try:
                    # 6:00 update
                    update6 = '$GME:' + '\n' + 'Price: $' + getStockData(today6)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 6:00 tweet
                    print('[gme bot: 6am ]', update6)
                    # tweet(update6)
                    time.sleep(timeLeft(today630, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 6am tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        ################
        ## 6:30 AM ET ##
        ################

        if today630 <= now:
            if now < today7:
                try:
                    # 6:30 update
                    update630 = '$GME:' + '\n' + 'Price: $' + getStockData(today630)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 6:30 tweet
                    print('[gme bot: 6:30am ]', update630)
                    # tweet(update630)
                    time.sleep(timeLeft(today7, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 6:30am tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        ################
        ## 7:00 AM ET ##
        ################

        if today7 <= now:
            if now < today730:
                try:
                    # 7:00 update
                    update7 = '$GME:' + '\n' + 'Price: $' + getStockData(today7)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 7:00 tweet
                    print('[gme bot: 7am ]', update7)
                    # tweet(update7)
                    time.sleep(timeLeft(today730, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 7am tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        ################
        ## 7:30 AM ET ##
        ################

        if today730 <= now:
            if now < today8:
                try:
                    # 7:30 update
                    update730 = '$GME:' + '\n' + 'Price: $' + getStockData(today730)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 7:30 tweet
                    print('[gme bot: 7:30am ]', update730)
                    # tweet(update730)
                    time.sleep(timeLeft(today8, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 7:30am tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        ################
        ## 8:00 AM ET ##
        ################

        if today8 <= now:
            if now < today830:
                try:
                    # 8:00 update
                    update8 = '$GME:' + '\n' + 'Price: $' + getStockData(today8)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 8:00 tweet
                    print('[gme bot: 8am ]', update8)
                    # tweet(update8)
                    time.sleep(timeLeft(today830, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 8am tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        ################
        ## 8:30 AM ET ##
        ################

        if today830 <= now:
            if now < today9:
                try:
                    # 8:30 update
                    update830 = '$GME:' + '\n' + 'Price: $' + getStockData(today830)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 8:30 tweet
                    print('[gme bot: 8:30am ]', update830)
                    # tweet(update830)
                    time.sleep(timeLeft(today9, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 8:30am tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        ################
        ## 9:00 AM ET ##
        ################

        if today9 <= now:
            if now < today930:
                try:
                    # 9:00 update
                    update9 = '$GME:' + '\n' + 'Price: $' + getStockData(today9)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 9:00 tweet
                    print('[gme bot: 9am ]', update9)
                    # tweet(update9)
                    time.sleep(timeLeft(today930, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 9am tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        ################
        ## 9:30 AM ET ##
        ################

        if today930 <= now:
            if now < today10:
                try:
                    # 9:30 update
                    update930 = '$GME:' + '\n' + 'Today is ' + day[wD] + '\n' + 'Opening Bell - 9:30 AM ET' + '\n' + 'Price: $' + getStockData(today4)[0] + '\n' + 'Volume: ' + getStockData(today930)[1] + ' [shares traded since open]'
                    # 9:30 tweet
                    print('[gme bot: 9:30am ]', update930)
                    # tweet(update930)
                    time.sleep(timeLeft(today10, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 9:30am tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 10:00 AM ET ##
        #################

        if today10 <= now:
            if now < today1030:
                try:
                    # 10:00 update
                    update10 = '$GME:' + '\n' + 'Price: $' + getStockData(today10)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 10:00 tweet
                    print('[gme bot: 10am ]', update10)
                    # tweet(update10)
                    time.sleep(timeLeft(today1030, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 10am tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 10:30 AM ET ##
        #################

        if today1030 <= now:
            if now < today11:
                try:
                    # 10:30 update
                    update1030 = '$GME:' + '\n' + 'Price: $' + getStockData(today1030)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 10:30 tweet
                    print('[gme bot: 10:30am ]', update1030)
                    # tweet(update1030)
                    time.sleep(timeLeft(today11, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 10:30am tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 11:00 AM ET ##
        #################

        if today11 <= now:
            if now < today1130:
                try:
                    # 11:00 update
                    update11 = '$GME:' + '\n' + 'Price: $' + getStockData(today11)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 11:00 tweet
                    print('[gme bot: 11am ]', update11)
                    # tweet(update11)
                    time.sleep(timeLeft(today1130, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 11am tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 11:30 AM ET ##
        #################

        if today1130 <= now:
            if now < today12:
                try:
                    # 11:30 update
                    update11 = '$GME:' + '\n' + 'Price: $' + getStockData(today1130)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 11:30 tweet
                    print('[gme bot: 11:30am ]', update1130)
                    # tweet(update1130)
                    time.sleep(timeLeft(today12, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 11:30am tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 12:00 PM ET ##
        #################

        if today12 <= now:
            if now < today1230:
                try:
                    # 12:00 update
                    update12 = '$GME:' + '\n' + 'Price: $' + getStockData(today12)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 12:00 tweet
                    print('[gme bot: 12pm ]', update12)
                    # tweet(update12)
                    time.sleep(timeLeft(today1230, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 12pm tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 12:30 PM ET ##
        #################

        if today1230 <= now:
            if now < today13:
                try:
                    # 12:30 update
                    update1230 = '$GME:' + '\n' + 'Price: $' + getStockData(today1230)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 12:30 tweet
                    print('[gme bot: 12:30pm ]', update1230)
                    # tweet(update1230)
                    time.sleep(timeLeft(today13, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 12:30pm tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 1:00 PM ET ##
        #################

        if today13 <= now:
            if now < today1330:
                try:
                    # 1:00 update
                    update13 = '$GME:' + '\n' + 'Price: $' + getStockData(today13)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 1:00 tweet
                    print('[gme bot: 1pm ]', update13)
                    # tweet(update13)
                    time.sleep(timeLeft(today1330, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 1pm tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 1:30 PM ET ##
        #################

        if today1330 <= now:
            if now < today14:
                try:
                    # 1:30 update
                    update1330 = '$GME:' + '\n' + 'Price: $' + getStockData(today1330)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 1:30 tweet
                    print('[gme bot: 1:30pm ]', update1330)
                    # tweet(update1330)
                    time.sleep(timeLeft(today14, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 1:30pm tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 2:00 PM ET ##
        #################

        if today14 <= now:
            if now < today1430:
                try:
                    # 2:00 update
                    update14 = '$GME:' + '\n' + 'Price: $' + getStockData(today14)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 2:00 tweet
                    print('[gme bot: 2pm ]', update14)
                    # tweet(update14)
                    time.sleep(timeLeft(today1430, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 2pm tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 2:30 PM ET ##
        #################

        if today1430 <= now:
            if now < today15:
                try:
                    # 2:30 update
                    update1430 = '$GME:' + '\n' + 'Price: $' + getStockData(today1430)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 2:30 tweet
                    print('[gme bot: 2:30pm ]', update1430)
                    # tweet(update1430)
                    time.sleep(timeLeft(today15, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 2:30pm tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 3:00 PM ET ##
        #################

        if today15 <= now:
            if now < today1530:
                try:
                    # 3:00 update
                    update15 = '$GME:' + '\n' + 'Power Hour!' + 'Price: $' + getStockData(today15)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 3:00 tweet
                    print('[gme bot: 3pm ]', update15)
                    # tweet(update15)
                    time.sleep(timeLeft(today1530, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 3pm tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 3:30 PM ET ##
        #################

        if today1530 <= now:
            if now < today16:
                try:
                    # 3:30 update
                    update1530 = '$GME:' + '\n' + 'Price: $' + getStockData(today1530)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 3:30 tweet
                    print('[gme bot: 3:30pm ]', update1530)
                    # tweet(update1530)
                    time.sleep(timeLeft(today16, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 3:30pm tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 4:00 PM ET ##
        #################

        if today16 <= now:
            if now < today1630:
                try:
                    # 4:00 update
                    update16 = '$GME:' + '\n' + 'Price: $' + getStockData(today16)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 4:00 tweet
                    print('[gme bot: 4pm ]', update16)
                    # tweet(update16)
                    time.sleep(timeLeft(today1630, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 4pm tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 4:30 PM ET ##
        #################

        if today1630 <= now:
            if now < today17:
                try:
                    # 4:30 update
                    update1630 = '$GME:' + '\n' + 'Price: $' + getStockData(today1630)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 4:30 tweet
                    print('[gme bot: 4:30pm ]', update1630)
                    # tweet(update1630)
                    time.sleep(timeLeft(today17, now))

                except Exception as e:
                    logging.error(str(e.__class__.__name__) + ": " + str(e), e)
                    print('[gme bot: 4:30pm tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 5:00 PM ET ##
        #################

        if today17 <= now:
            if now < today1730:
                try:
                    # 5:00 update
                    update17 = '$GME:' + '\n' + 'Price: $' + getStockData(today17)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 5:00 tweet
                    print('[gme bot: 5pm ]', update17)
                    # tweet(update17)
                    time.sleep(timeLeft(today1730, now))

                except Exception as e:
                    print('[gme bot: 5pm tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 5:30 PM ET ##
        #################

        if today1730 <= now:
            if now < today18:
                try:
                    # 5:30 update
                    update1730 = '$GME:' + '\n' + 'Price: $' + getStockData(today1730)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 5:30 tweet
                    print('[gme bot: 5:30pm ]', update1730)
                    # tweet(update1730)
                    time.sleep(timeLeft(today18, now))

                except Exception as e:
                    print('[gme bot: 5:30pm tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 6:00 PM ET ##
        #################

        if today18 <= now:
            if now < today1830:
                try:
                    # 6:00 update
                    update18 = '$GME:' + '\n' + 'Price: $' + getStockData(today18)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 6:00 tweet
                    print('[gme bot: 6pm ]', update18)
                    # tweet(update18)
                    time.sleep(timeLeft(today1830, now))

                except Exception as e:
                    print('[gme bot: 6pm tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 6:30 PM ET ##
        #################

        if today1830 <= now:
            if now < today19:
                try:
                    # 6:30 update
                    update18 = '$GME:' + '\n' + 'Price: $' + getStockData(today1830)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 6:30 tweet
                    print('[gme bot: 6:30pm ]', update1830)
                    # tweet(update1830)
                    time.sleep(timeLeft(today19, now))

                except Exception as e:
                    print('[gme bot: 6:30pm tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(30)


        #################
        ## 7:00 PM ET ##
        #################

        if today19 <= now:
            if now < today1930:
                try:
                    # 7:00 update
                    update18 = '$GME:' + '\n' + 'Price: $' + getStockData(today19)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 7:00 tweet
                    print('[gme bot: 7pm ]', update19)
                    # tweet(update19)
                    time.sleep(timeLeft(today1930, now))

                except Exception as e:
                    print('[gme bot: 7pm tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(30)


        #################
        ## 7:30 PM ET ##
        #################

        if today1930 <= now:
            if now < today20:
                try:
                    # 7:30 update
                    update18 = '$GME:' + '\n' + 'Price: $' + getStockData(today1930)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                    # 7:30 tweet
                    print('[gme bot: 7:30pm ]', update1930)
                    # tweet(update1930)
                    time.sleep(timeLeft(today20, now))

                except Exception as e:
                    print('[gme bot: 7:30pm tweet | data is likely not ready. waiting a minute...]')
                    time.sleep(60)


        #################
        ## 8:00 PM ET ##
        #################

        if today20 <= now:
            try:
                # 8:00 update
                update18 = '$GME:' + '\n' + 'Price: $' + getStockData(today20)[0] + '\n' + 'Volume: ' + getStockData(today4)[1] + ' [shares traded since open]'
                # 8:00 tweet
                print('[gme bot: 8pm ]', update20)
                # tweet(update20)
                time.sleep(3600)

            except Exception as e:
                print('[gme bot: 8pm tweet | data is likely not ready. waiting a minute...]')
                time.sleep(60)



        #
        #
        # # #################
        # # # German Market #
        # # #################
        #
        # # 2:00 AM ET - Opening bell
