import os
from typing import List

from openai import OpenAI

from model import State


def ask_ai(messages: List):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url=os.environ.get("OPENAI_API_URL"),
    )

    response = client.chat.completions.create(
        model=os.environ.get("OPENAI_MODEL"),
        messages=messages
    )

    return response.choices[0].message.content


def node_chatbot(state: State):
    return {
        "messages": [
            ask_ai(state['messages']),
        ]
    }
