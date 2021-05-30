from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

import config
import schemas
import functions
import json
import tweepy


def getAPI():
    try:
        api = config.createAPI()
        yield api
    except Exception as e:
        print(f'[-] {e}')


app = FastAPI()


@app.get('/getstatus/{username}/{num_page}', response_model=schemas.Tweet)
def getstatus(username: str, num_page: int, api=Depends(getAPI)):
    tweet_list = []

    for page in range(num_page):
        try:
            user_timeline = api.user_timeline(
                username, page=page, tweet_mode="extended")
            tweet_list += functions.makeList(user_timeline)
        except tweepy.error.TweepError as e:
            if e['code'] == 34:
                raise HTTPException(status_code='404', detail=f'{e["message"]}')
            elif e == 'Not authorized.':
                raise HTTPException(status_code='403', detail=f'{e["Account is private"]}')

    results = {
        'username': username,
        'tweet': tweet_list
    }

    return results
