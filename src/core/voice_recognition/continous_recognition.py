  # server.py

import socket
import wave
from io import BytesIO
import speech_recognition as sr

from src.core.voice_recognition.consts import RESPEAKER_RATE, RESPEAKER_WIDTH

HOST = "192.168.0.133"  # Replace with your PC's IP address
PORT = 12345
from faster_whisper import WhisperModel


def save_audio(data):
    with wave.open("received_audio.wav", "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(44100)
        wf.writeframes(data)


model = WhisperModel("medium", device="cpu", compute_type="int8")


def recognize(audio_frames):
    audio_data = sr.AudioData(audio_frames, RESPEAKER_RATE, RESPEAKER_WIDTH)
    segments, _ = model.transcribe(BytesIO(audio_data.get_wav_data()))
    return " ".join([segment.text for segment in segments])


def main():
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((HOST, PORT))
            server_socket.listen()

            print(f"Listening on {HOST}:{PORT}")

            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")

                audio_data = b""
                while True:
                    chunk = conn.recv(1024)
                    if not chunk:
                        break
                    audio_data += chunk

                    if len(audio_data) >= 44100:
                        recognized = recognize(audio_data)
                        print(recognized)
                        audio_data = b""

    print("Server closed.")


if __name__ == "__main__":
    main()
