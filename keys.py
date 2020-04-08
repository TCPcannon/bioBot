import tweepy

# Make it easier on myself
'''Use your access and authentication tokens from Twitter developer account'''
auth = tweepy.OAuthHandler("[]", "[]")
auth.set_access_token("[]", "[]")

# Authenticate to Twitter
def getApi() :
    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
