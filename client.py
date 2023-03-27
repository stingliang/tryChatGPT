# -*- encoding: utf-8 -*-
"""
@File    : client.py
@Time    : 2023/3/27 23:33
@Author  : liangrui
@Email   : liangrui5526@aiforail.com
@Software: PyCharm
"""

import requests
import json


class RPCClient:
    def __init__(self, url):
        self.url = url

    def ask(self, prompt: str):
        payload = {
            "jsonrpc": "2.0",
            "method": "ask",
            "params": [prompt],
            "id": 0,
        }
        response = requests.post(self.url, data=json.dumps(payload))
        return response.json()['result']


if __name__ == '__main__':
    client = RPCClient(url='http://localhost:8080')
    while True:
        what_did_you_say = input('You: ')
        print(f'AI: {client.ask(what_did_you_say)}')
