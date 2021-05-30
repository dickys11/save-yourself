import re
import emoji

def makeList(user_timeline):
    tweet_list = []
    tweet_dict  = {}
    for tweet in user_timeline:
        tweet_dict['text'] = cleanTweet(tweet._json['full_text'])
        tweet_dict['created_at'] = tweet._json['created_at']
        tweet_dict['id'] = tweet._json['id']
        tweet_dict_copy = tweet_dict.copy()
        tweet_list.append(tweet_dict_copy)

    return tweet_list

def cleanTweet(tweet):
    tweet = re.sub("@[A-Za-z0-9]+","",tweet) #Remove @ sign
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet) #Remove http links
    tweet = " ".join(tweet.split())
    tweet = ''.join(c for c in tweet if c not in emoji.EMOJI_ALIAS_UNICODE_ENGLISH.values()) #Remove Emojis
    tweet = tweet.replace("#", "").replace("_", " ") #Remove hashtag sign but keep the text
    tweet = tweet.encode('ascii', 'ignore') #Remove non ascii character
    tweet = tweet.lower() #Lowercase

    return tweet