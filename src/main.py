import ast
import re

from src.modules.assistant.open_ai_assistatnt import OpenAIChatBot
from src.modules.user_communication.communication import UserCommunication
from src.modules.voice_recognition.voice_recognition import SpeechRecognition
from src.modules.youtube.youtube import YoutubeConnector

COMMANDS = {
    "search_and_play_video": YoutubeConnector.search_and_play_video,
    "respond_to_user": UserCommunication.respond,
}


def main():
    model_name = "gpt-3.5-turbo"

    chatbot = OpenAIChatBot(model_name)
    recognition = SpeechRecognition()

    recognition.listen()
    human_order = recognition.recognize()
    output = chatbot.chat(human_order)
    print(output)

    function_name = re.sub(r"[^a-zA-Z0-9_]", "", output.split("\n")[0])
    parameters = " ".join(output.split("\n")[1:])

    COMMANDS[function_name](**ast.literal_eval(parameters))


if __name__ == "__main__":
    main()
