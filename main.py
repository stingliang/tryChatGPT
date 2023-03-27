# -*- encoding: utf-8 -*-
"""
@File    : main.py
@Time    : 2023/3/27 22:42
@Author  : liangrui
@Email   : liangrui5526@aiforail.com
@Software: PyCharm
"""

import chat

if __name__ == '__main__':
    chat_gpt = chat.Chat(api_key_path='/home/liangrui/openai/openai.key')
    while True:
        prompt = input('You: ')
        chat_gpt.ask(prompt)
