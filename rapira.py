from decimal import Decimal

import requests


def fetch_rate() -> Decimal:
    api_url = "https://api.rapira.net/open/market/rates"
    resp = requests.get(api_url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    rate = data["data"][0]
    if rate["symbol"] != "USDT/RUB":
        raise AttributeError
    return Decimal(str(rate["close"]))
