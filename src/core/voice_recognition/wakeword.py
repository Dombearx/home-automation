from pathlib import Path

import numpy as np
import pyaudio
from openwakeword.model import Model

from src.core.voice_recognition.consts import (RESPEAKER_CHANNELS,
                                               RESPEAKER_RATE, RESPEAKER_WIDTH)

current_dir = Path(__file__).parent


class WakeWord:
    def __init__(self):
        # self.wake_word_model = Model(
        #     wakeword_models=[f"{current_dir}/models/thanks.onnx"],
        # )
        self.end_word_model = Model(
            wakeword_models=[f"{current_dir}/models/thanks.onnx"],
        )
        self.wake_word_model = Model(
            wakeword_models=[f"alexa"],
        )
        # self.end_word_model = Model(
        #     wakeword_models=[f"alexa"],
        # )
        audio = pyaudio.PyAudio()
        self.input_stream = audio.open(
            format=audio.get_format_from_width(RESPEAKER_WIDTH),
            channels=RESPEAKER_CHANNELS,
            rate=RESPEAKER_RATE,
            input=True,
        )

    def listen(self):
        print("listening...")
        while True:
            data = self.input_stream.read(CHUNK)
            numpy_data = np.frombuffer(data, dtype=np.int16)
            prediction = self.wake_word_model.predict(numpy_data)
            if prediction["alexa"] > 0.8:
                break

    def record(self):
        last_audio = []
        print("recording_audio")
        while True:
            data = self.input_stream.read(CHUNK)
            numpy_data = np.frombuffer(data, dtype=np.int16)
            last_audio.append(data)
            prediction = self.end_word_model.predict(numpy_data)
            if prediction["thanks"] > 0.15:
                print("audio recorded")
                return last_audio
