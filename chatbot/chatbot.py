from chatbot.rules import RULES, DEFAULT_RESPONSE


class ChatBot:
    """
    A simple rule-based chatbot.

    """

    def get_response(self, message: str) -> str:
        """
        Process a user message and return a response.
        
        """

        normalized_message = message.strip().lower()

        if normalized_message in RULES:
            return RULES[normalized_message]

        return DEFAULT_RESPONSE