from fastapi import FastAPI, Depends, HTTPException, status
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
        except tweepy.TweepError as e:
            if e.api_code == 34:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail=e.response)
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    results = {
        'username': username,
        'tweet': tweet_list
    }

    return results
