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
    human_order = "how many letters in the word educa?"
    human_order = "Play no mercy by the living tombstone"
    output = chatbot.chat(human_order)
    print(output)


if __name__ == "__main__":
    main()
