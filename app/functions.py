import re
import emoji
import config
import tensorflow as tf


def makeList(user_timeline):
    tweet_list = []
    tweet_dict  = {}
    for tweet in user_timeline:
        text = tweet.full_text.lower() #Lowercase
        if filterTweet(text):
            clean_text = cleanTweet(tweet.full_text)
            print(f'[+] {clean_text}')
            tweet_dict['text'] = clean_text
            tweet_dict['created_at'] = tweet.created_at
            tweet_dict['id'] = tweet.id_str
            tweet_dict['prediction'] = predict(clean_text).astype(float)
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

    return tweet

def filterTweet(tweet):
    for keyword in config.KEYWORDS:
        if (keyword in tweet) and ('RT @' not in tweet):
            return True

def predict(tweet):
    prediction = config.MODEL.predict([tweet])
    # prediction = tweet.decode("utf-8")
    return prediction[0][0]