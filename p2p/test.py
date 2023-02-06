import requests
url = "https://api.exmo.com/v1.1/trades"
data = {
    "pair": "BTC_USD"
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}


response = requests.post(url, headers=headers, data=data)

print(response.text)

