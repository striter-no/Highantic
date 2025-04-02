from src.backend.conversation import *

if __name__ == '__main__':
    conversation = Conversation()

    status, ans = conversation.ask_text(
        "Привет, кто ты?",
        files = [],
        images = [],
        specified_provider=gpt.provider_stock.PollinationsAI.__name__
    )

    print(ans)