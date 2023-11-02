from langchain.chat_models import ChatOpenAI

from src.modules.assistant.assistant_template import ChatBotTemplate


class OpenAIChatBot(ChatBotTemplate):
    def __init__(self, model_name: str):
        main_llm = ChatOpenAI(model_name=model_name, temperature=0)
        super().__init__(main_llm)
