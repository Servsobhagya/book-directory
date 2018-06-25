#What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).
#access token
An access token is an object that describes the security context of a process or thread. The information in a token includes the identity and privileges of the user account associated with the process or thread

#Generate your access token for any API.
	create account on twitter
	Go to https://dev.twitter.com/apps/new and log in, if necessary
Enter your Application Name, Description and your website address. You can leave the callback URL empty.
Accept the TOS, and solve the CAPTCHA.
Submit the form by clicking the Create your Twitter Application
Copy the consumer key (API key) and consumer secret from the screen into your application





#Get the IP address of some common sites like Google, Facebook by using DNS lookup
# Name:    google.com
# Addresses:  2404:6800:4002:806::200e
          # 172.217.31.14
# Name:    facebook.com
# Addresses:  2a03:2880:f126:83:face:b00c:0:25de
          # 157.240.16.35

#Using Tweepy library try to extract tweets from Twitter.
import tweepy
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
tweets=api.search ('#nda',lang='en',count=10, tweet_mode="extended")
#print tweets
for tweet in tweets:
	print("a")
	print(tweet.full_text)
	print("a")

#What is a difference between library and API . Figure it out with examples.
API is a part of library which defines how an application communicates with external code
.
API can be written in any language.
for example:Uber ,Ola uses Google Maps API to show navigations and ways .
API can be used to Get , create , update and delete the data.


#library
Library is written in same language which is a collection of all the functionalities required for the use case
For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
		  