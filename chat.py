# -*- encoding: utf-8 -*-
"""
@File    : chat.py
@Time    : 2023/3/21 20:20
@Author  : liangrui
@Email   : liangrui5526@aiforail.com
@Software: PyCharm
"""

import openai


class Chat:

    def __init__(self, api_key_path: str, model: str = 'gpt-3.5-turbo', conversation_list=None) -> None:
        """
        初始化
        :param api_key_path:
        :param model:
        :param conversation_list: 初始化对话列表，可以加入一个key为system的字典，有助于形成更加个性化的回答
        self.conversation_list = [{'role':'system','content':'你是一个非常友善的助手'}]
        """
        self.api_key_path = api_key_path
        self.model = model
        self.set_credentials()
        self.token = 0
        if conversation_list is None:
            conversation_list = []
        self.conversation_list = conversation_list

    def set_credentials(self):
        openai.api_key_path = self.api_key_path

    def show_conversation(self, msg_list):
        """
        展示对话
        :param msg_list:
        :return:
        """
        print(f'AI: {msg_list[-1]["content"]}(token cost: {self.token})')

    def ask(self, prompt):
        """
        问问题
        :param prompt: 问题描述
        :return:
        """
        self.conversation_list.append({'role': 'user', 'content': prompt})
        response = openai.ChatCompletion.create(model=self.model, messages=self.conversation_list)
        answer = response.choices[0].message['content']
        # 统计token消耗量
        self.token += int(response['usage']['total_tokens'])
        # 下面这一步是把chatGPT的回答也添加到对话列表中，这样下一次问问题的时候就能形成上下文了
        self.conversation_list.append({'role': 'assistant', 'content': answer})
        self.show_conversation(self.conversation_list)
