from typing import Union

from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/roleUsers/{encryptedToken}")
def read_item(encryptedToken: str):
    url = 'https://62fc4666abd610251c17fdae.mockapi.io/api/roleUsers?encryptedToken='+encryptedToken
    response = requests.get(url, {}, timeout=5)
    return {"items": response.json()}
