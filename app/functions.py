def makeList(user_timeline):
    tweet_list = []
    tweet_dict  = {}
    for tweet in user_timeline:
        tweet_dict['created_at'] = tweet._json['created_at']
        tweet_dict['text'] = tweet._json['full_text']
        tweet_dict_copy = tweet_dict.copy()
        tweet_list.append(tweet_dict_copy)

    return tweet_list