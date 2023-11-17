from src.modules.assistant.open_ai_assistatnt import OpenAIChatBot
from src.modules.voice_recognition.voice_recognition import SpeechRecognition
from src.modules.voice_recognition.wakeword import WakeWord


def main():
    model_name = "gpt-3.5-turbo"

    OpenAIChatBot(model_name)
    recognition = SpeechRecognition()
    voice_capture = WakeWord()

    voice_capture.listen()
    audio = voice_capture.record()

    human_order = recognition.recognize(audio)
    # human_order = "how many letters in the word educa?"
    # human_order = "Remind me to buy onion, two carrots, milk and a meat"
    # human_order = "Remind me that i should buy milk"
    print(human_order)
    # chatbot.chat(human_order)


if __name__ == "__main__":
    main()
