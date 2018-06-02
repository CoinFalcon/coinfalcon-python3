import hashlib
import requests
import urllib
import urllib.parse
import json
import hmac
import time

class CoinFalcon():

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.endpoint = 'https://staging.coinfalcon.com/api/v1'

    def request_path(self, url):
        query = urllib.parse.urlparse(url).query
        if query == '':
            return urllib.parse.urlparse(url).path
        return urllib.parse.urlparse(url).path + '?' + query

    def get_headers(self, method, request_path, body={}):
        timestamp = str(int(time.time()))

        if method == 'GET':
            payload = '|'.join([timestamp, method, request_path])
        else:
            payload = '|'.join([timestamp, method, request_path, json.dumps(body, separators=(',', ':'))])

        print(payload)
        message = bytes(payload, 'utf-8')
        secret = bytes(self.secret, 'utf-8')

        signature = hmac.new(secret, message, hashlib.sha256).hexdigest()
        return {
            "CF-API-KEY": self.key,
            "CF-API-TIMESTAMP": timestamp,
            "CF-API-SIGNATURE": signature
        }

    def create_order(self, body):
        url = self.endpoint + "/user/orders"
        headers = self.get_headers('POST', urllib.parse.urlparse(url).path, body)
        return requests.post(url, headers=headers, data=body).json()

    def cancel_order(self, id):
        url = self.endpoint + "/user/orders/{}".format(id)
        print(url)
        headers = self.get_headers('DELETE', urllib.parse.urlparse(url).path, {})
        return requests.delete(url, headers=headers).json()

    def my_orders(self):
        url = self.endpoint + "/user/orders"
        headers = self.get_headers('GET', urllib.parse.urlparse(url).path)
        return requests.get(url, headers=headers).json()

    def deposit_address(self, currency):
        url = self.endpoint + "/account/deposit_address?currency={}".format(currency)
        headers = self.get_headers('GET', self.request_path(url))
        return requests.get(url, headers=headers).json()

    def orderbook(self, market):
        url = self.endpoint + "/markets/{}/orders".format(market)
        print(url)
        print(requests.get(url).text)
        return requests.get(url).json()

# client = CoinFalcon('abf59bd6-7270-453f-9ae0-89f8cb879d3f', 'd35d0298-8b27-4255-8750-50619da67a65')
# print(client.orderbook('IOT-BTC'))
# print(client.my_orders())
# result = client.create_order({'market': 'BTC-EUR', 'operation_type': 'market_order', 'order_type': 'sell', 'size': '0.1'})
# print(result)
# print(client.cancel_order(result['data']['id']))
# print(client.deposit_address('btc'))
