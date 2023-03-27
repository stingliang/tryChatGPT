# -*- encoding: utf-8 -*-
"""
@File    : server.py
@Time    : 2023/3/27 22:42
@Author  : liangrui
@Email   : liangrui5526@aiforail.com
@Software: PyCharm
"""

import chat
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jsonrpc import JSONRPCResponseManager, dispatcher

if __name__ == '__main__':
    chat_gpt = chat.Chat(api_key_path="/home/liangrui/openai/openai.key")

    @dispatcher.add_method
    def ask(prompt):
        response = chat_gpt.ask(prompt)
        return response

    @Request.application
    def application(request):
        # Dispatcher is dictionary {<method_name>: callable}
        response = JSONRPCResponseManager.handle(
            request.data, dispatcher)
        return Response(response.json, mimetype='application/json')

    run_simple('localhost', 8080, application)
