# Some common Twitter tasks

import json
import tweepy
from tweepy import OAuthHandler

# Consumer keys and access tokens, used for OAuth
consumer_key = 'TrO4IfH1matnZACyX569JESGk'
consumer_secret = 'xBQNcFa7VTfNKQqbOz3WHhsrM7KTVWoymcnGo2pnTDnnvsPGNs'
access_token = '14104457-ITs2bJ4TH4XPYT1MqeEJx8WOcKsbeKvWItd30bMWR'
access_token_secret = 'hX5rbKjOG09iSgRrSi7l4czUmoPhLbBS7DMzGH0JFNMJz'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)

def process_or_store(tweet):
   print(json.dumps(tweet))

# Read our own timeline (our Twitter home page)

# for status in tweepy.Cursor(api.home_timeline).items(10):
#     # Process a single status
#     process_or_store(status._json) 


# View list of all of our followers

#for friend in tweepy.Cursor(api.friends).items():
#    process_or_store(friend._json)


# View list of all of our followers (only screen names)

user = api.get_user('rdomanski')
print ("Retrieving friends for:", user.screen_name)
for friend in tweepy.Cursor(api.friends).items():
	print ("\n", friend.screen_name)


# View list of all our tweets

#for tweet in tweepy.Cursor(api.user_timeline).items():
#    process_or_store(tweet._json)


# View list of all of our followers IDs
#     print api.followers_ids('rdomanski')


# View list of all of our friends (people who we follow)
# This displays 20 at a time

# friends = api.friends()
# for friend in friends:
# 	print friend.name

# This displays all friends
# for page in tweepy.Cursor(api.friends).pages():
#     for friend in page:
#     	print friend.name


# View our timeline

# timeline = api.home_timeline()
 
# for item in timeline:
#     text = "%s says '%s'" % (item.user.screen_name, item.text)
#     print "\n", text


# Display the last 20 tweets by another user (ex. - @lessig)
# lessig_tweets = api.user_timeline('lessig')
# for tweet in lessig_tweets:
# 	print (tweet.created_at)
# 	print (tweet.text)


