from langchain.chat_models.base import BaseChatModel
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


class ChatBotTemplate:
    def __init__(self, main_llm: BaseChatModel):

        template = """
            You are a home assistant.
            You will get a list of possible functions with their documentation.
            Your goal is to listen to human orders and respond with function name with parameters that will best suit the human needs.
            Interpret the command based on your own knowledge; for example, when user asks for something sweet respond with candies or chocolate bar.
            Be descriptive when filling functions parameters.
            In the first line of response send only the function name.
            In the second line send parameters formatted as python dict.
            
            EXAMPLE
            human: play some classic polish rap
            assistant:search_and_play_video()
            {{
                "text_to_search": "paktofonika"
            }}
            END OF EXAMPLE
            
            LIST OF FUNCTIONS
            
            name: search_and_play_video - allows to play youtube video
            attributes: text_to_search: str - text that will be used for search, should be short and concise
            
            name: respond_to_user - allows to respond to user
            attributes: response: str - text that will be said to user
            
            END OF LIST OF FUNCTIONS
            
            human: {human_input}
            assistant:
        """

        prompt = PromptTemplate(
            input_variables=["human_input"],
            template=template,
        )

        self.chat_chain = LLMChain(
            llm=main_llm,
            prompt=prompt,
            verbose=True,
        )


    def chat(self, human_input: str):
        output = self.chat_chain.predict(human_input=human_input)
        return output

