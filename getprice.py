import requests
import json
import os

resp = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ANS&tsyms=USD")
data = json.loads(resp.text)


if os.getenv("PROD"):
    json_path = "/var/www/neoprice.org/app/static/prices.json"
else:
    json_path = "/Users/kekearif/Documents/neoprice.org/app/static/prices.json"
with open(json_path, 'w') as outfile:
    json.dump(data, outfile)
