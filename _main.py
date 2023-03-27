import openai


class ChatGPT:
    PROMPT_PREFIX = (
            "Do not return me any English sentence." +
            "Summarize the following description into a list of points as simplified Chinese. "
    )

    def __init__(self, api_key_path: str, model: str = "text-davinci-003"):
        self.api_key_path = api_key_path
        self.model = model
        self.set_credentials()

    def set_credentials(self):
        openai.api_key_path = self.api_key_path

    def summarize(self, summary, max_tokens: int = 1024):
        # Set up the model and prompt
        prompt = f"{self.PROMPT_PREFIX}\n{summary}"

        # Generate a response
        completion = openai.Completion.create(
            engine=self.model,
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completion.choices[0].text
        return response


if __name__ == '__main__':
    chat_gpt = ChatGPT(api_key_path="/home/liangrui/openai/openai.key")
    summary = [
        '完成了一个简单的聊天机器人,用到了openai的api和python的类'
    ]
    print(chat_gpt.summarize(summary))
