from io import BytesIO
from pathlib import Path

import speech_recognition as sr
from faster_whisper import WhisperModel

current_dir = Path(__file__).parent


class SpeechRecognition:
    def __init__(self, model_size: str = "medium"):
        self.last_audio = None
        self.recognizer = sr.Recognizer()
        self.model = WhisperModel(model_size, device="cpu", compute_type="int8")

    def listen(self):
        with sr.Microphone() as source:
            print("Say something!")
            self.last_audio = self.recognizer.listen(source)

    def recognize(self):
        segments, _ = self.model.transcribe(BytesIO(self.last_audio.get_wav_data()))
        return " ".join([segment.text for segment in segments])
