import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("BINANCE_KEY")
api_secret = os.getenv("BINANCE_SEC")