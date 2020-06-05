# import Twython module to send tweets
from twython import Twython

# import variables
from auth import (
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret
)

# import up-to-date coronavirus data
import COVID19Py

# make connection with the Twitter API
twitter = Twython (
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret
)

# test connection with basic tweet
tweet = "My first tweet!"
twitter.update_status(status=tweet)
print("Tweet successfully sent: " + tweet)


# create new instance
covid19 = COVID19Py.COVID19()

# getting the latest confirmed statistics
latestStats = covid19.getLatest()

# getting location by country code
location = covid19.getLocationByCountryCode("BE")

# tweet corona statistics
"""
tweet =
twitter.update_status(status=tweet)
print("Tweet successfully sent: " + tweet)
"""