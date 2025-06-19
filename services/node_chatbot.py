import os
from typing import List

from langchain_google_genai import ChatGoogleGenerativeAI

from model import State


def ask_ai(messages: List):
    client = ChatGoogleGenerativeAI(
        google_api_key=os.environ.get("OPENAI_API_KEY"),
        model=os.environ.get("OPENAI_MODEL"),
    )

    response = client.invoke(messages)
    return response


def node_chatbot(state: State):
    return {
        "messages": [
            ask_ai(state.messages),
        ]
    }
