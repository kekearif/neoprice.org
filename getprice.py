import requests
import json

resp = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ANS&tsyms=BTC,USD")
data = json.loads(resp.text)
with open('app/static/prices.json', 'w') as outfile:
    json.dump(data, outfile)
