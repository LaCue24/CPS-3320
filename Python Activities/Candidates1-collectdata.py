# Remember to use the command Candidates1-collectdata.py > twitter_data.txt to pipe the output to a new file

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Consumer keys and access tokens, used for OAuth
consumer_key = 'TrO4IfH1matnZACyX569JESGk'
consumer_secret = 'xBQNcFa7VTfNKQqbOz3WHhsrM7KTVWoymcnGo2pnTDnnvsPGNs'
access_token = '14104457-ITs2bJ4TH4XPYT1MqeEJx8WOcKsbeKvWItd30bMWR'
access_token_secret = 'hX5rbKjOG09iSgRrSi7l4czUmoPhLbBS7DMzGH0JFNMJz'
 
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keyword: 'trump'
    stream.filter(track=['Trump'])