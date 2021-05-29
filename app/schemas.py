from typing import Optional, List
from pydantic import BaseModel

class Tweet(BaseModel):
    username: str
    tweet: List