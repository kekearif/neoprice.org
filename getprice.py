import requests
import json

resp = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ANS&tsyms=USD")
data = json.loads(resp.text)
with open('app/static/prices.json', 'w') as outfile:
    json.dump(data, outfile)
