from src.modules.assistant.open_ai_assistatnt import OpenAIChatBot
from src.modules.voice_recognition.voice_recognition import SpeechRecognition


def main():
    model_name = "gpt-3.5-turbo"

    chatbot = OpenAIChatBot(model_name)
    recognition = SpeechRecognition()

    recognition.listen()
    human_order = recognition.recognize()
    # human_order = "how many letters in the word educa?"
    # human_order = "Remind me to buy onion, two carrots, milk and a meat"
    # human_order = "Remind me that i should buy milk"
    chatbot.chat(human_order)


if __name__ == "__main__":
    main()
