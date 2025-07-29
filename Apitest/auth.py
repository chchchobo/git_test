# auth.py
import requests
import time
import logging
from fastapi import HTTPException
from config import CLIENT_ID, CLIENT_SECRET, TOKEN_URL

access_token = None
token_expiry = 0

def get_access_token():
    global access_token, token_expiry
    now = int(time.time())
    if access_token and token_expiry > now:
        return access_token

    data = {"grant_type": "client_credentials"}
    auth = (CLIENT_ID, CLIENT_SECRET)
    try:
        res = requests.post(TOKEN_URL, data=data, auth=auth)
        res.raise_for_status()
        token_data = res.json()
        access_token = token_data["access_token"]
        token_expiry = now + int(token_data.get("expires_in", 3600)) - 60
        return access_token
    except Exception as e:
        logging.error("Failed to get access token: %s", e)
        raise HTTPException(status_code=500, detail="OAuth token error")
