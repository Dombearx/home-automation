import os
import sys
from pathlib import Path

from fastapi import FastAPI, File, UploadFile

from src.modules.assistant.open_ai_assistatnt import OpenAIChatBot
from src.modules.voice_recognition.voice_recognition import SpeechRecognition

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, this is the root endpoint!"}


@app.post("/receive_audio")
def receive_audio(item: dict, file: UploadFile = File(...)):
    try:
        file_path = Path("tmp_filename.3gp")
        with file_path.open("wb") as buffer:
            buffer.write(file.file.read())

        os.system("ffmpeg -y -i tmp_filename.3gp tmp_filename.wav")
        print("Start file processing", file=sys.stderr)
        recognize()
        return "Audio received successfully"
    except Exception as e:
        print(f"Error: {e}")

        return "Error receiving audio", 500


def recognize():
    model_name = "gpt-3.5-turbo"
    chatbot = OpenAIChatBot(model_name)
    recognition = SpeechRecognition()
    human_order = recognition.recognize_from_file("tmp_filename.wav")
    print(human_order, file=sys.stderr)
    chatbot.chat(human_order)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
