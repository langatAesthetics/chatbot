# main.py

from chatbot.chatbot import ChatBot


def main():
    """
    Start the chatbot.
    
    """

    bot = ChatBot()

    print("=" * 50)
    print("Simple Python Chatbot")
    print("Type 'exit' to quit.")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ")

        if user_input.strip().lower() == "exit":
            print("Bot: Goodbye!")
            break

        response = bot.get_response(user_input)

        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
    