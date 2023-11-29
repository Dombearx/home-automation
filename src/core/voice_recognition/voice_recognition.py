from io import BytesIO

import speech_recognition as sr
from faster_whisper import WhisperModel

from src.core.voice_recognition.consts import RESPEAKER_RATE, RESPEAKER_WIDTH


class SpeechRecognition:
    def __init__(self, model_size: str = "medium"):
        self.model = WhisperModel(model_size, device="cpu", compute_type="int8")

    def recognize(self, audio_frames):
        audio_data = sr.AudioData(
            b"".join(audio_frames), RESPEAKER_RATE, RESPEAKER_WIDTH
        )
        segments, _ = self.model.transcribe(BytesIO(audio_data.get_wav_data()))
        return " ".join([segment.text for segment in segments])

    def recognize_from_file(self, file_path):
        segments, _ = self.model.transcribe(file_path)
        return " ".join([segment.text for segment in segments])
