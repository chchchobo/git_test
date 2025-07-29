# config.py
import os

CLIENT_ID = os.getenv("PCC_CLIENT_ID", "YOUR_CLIENT_ID")
CLIENT_SECRET = os.getenv("PCC_CLIENT_SECRET", "YOUR_CLIENT_SECRET")
TOKEN_URL = "https://fedlogin.cat.com/as/token.oauth2"
TRACKING_URL = "https://api.cat.com/eCommerce/orderTracking/v3/tracking?storeId=21801"
