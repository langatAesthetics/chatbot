import json
import random

from chatbot.nlp import tokenize
from chatbot.nlp import stem_tokens


class ChatBot:
    def __init__(self):
        with open(
            "chatbot/intents.json",
            "r",
            encoding="utf-8"
        ) as file:
            self.intents = json.load(file)

    def get_response(self, message: str) -> str:
        tokens = tokenize(message)
        tokens = stem_tokens(tokens)

        print(f"Tokens: {tokens}")

        for intent in self.intents["intents"]:
            for pattern in intent["patterns"]:
                pattern_tokens = tokenize(pattern)
                pattern_tokens = stem_tokens(pattern_tokens)

                if all(
                    token in tokens
                    for token in pattern_tokens
                ):
                    return random.choice(
                        intent["responses"]
                    )

        return (
            "I'm sorry, I don't understand that yet."
        )