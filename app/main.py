from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

import config
import schemas
import functions
import json

def getAPI():
    try:
        api = config.createAPI()
        yield api
    except Exception as e:
        print(f'[-] {e}')

