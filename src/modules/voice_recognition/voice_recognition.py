import speech_recognition as sr


class SpeechRecognition:
    def __init__(self):
        self.last_audio = None
        self.recognizer = sr.Recognizer()

    def listen(self):
        pass
        # with sr.Microphone() as source:
        #     print("Say something!")
        #     self.last_audio = self.recognizer.listen(source)

    def recognize(self):
        return "Hello this is my message"
        # try:
        #     recognized_text = self.recognizer.recognize_whisper(
        #         self.last_audio, language="english"
        #     )
        #     print("Whisper thinks you said " + recognized_text)
        #     return recognized_text
        # except sr.UnknownValueError:
        #     print("Whisper could not understand audio")
        # except sr.RequestError as e:
        #     print("Could not request results from Whisper")
