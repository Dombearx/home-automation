import logging
import time
from io import BytesIO

from fastapi import Depends, FastAPI, File, Form, Request, UploadFile, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from loguru import logger

from src.modules.assistant.open_ai_assistatnt import OpenAIChatBot
from src.modules.voice_recognition.voice_recognition import SpeechRecognition

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    exc_str = f"{exc}".replace("\n", " ").replace("   ", " ")
    logging.error(f"{request}: {exc_str}")
    content = {"status_code": 10422, "message": exc_str, "data": None}
    return JSONResponse(
        content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )


# Define a function to load your big data
def load_chatbot():
    model_name = "gpt-3.5-turbo"
    return OpenAIChatBot(model_name)


def load_recognition():
    recognition = SpeechRecognition("medium")
    return recognition


# Use a dependency to load the big data and store it in the app instance
async def get_chatbot(app: FastAPI = Depends(load_chatbot)):
    return app


async def get_recognition(app: FastAPI = Depends(load_recognition)):
    return app


@app.get("/")
def read_root():
    return {"message": "Hello, this is the root endpoint!"}


@app.post("/receive_audio")
def receive_audio(
    audioFile: UploadFile = File(...),
    chatbot: OpenAIChatBot = Depends(get_chatbot),
    recognition: SpeechRecognition = Depends(get_recognition),
):
    start_time = time.time()
    human_order = recognition.recognize_from_file(BytesIO(audioFile.file.read()))
    logger.debug(f"Audio processed in {time.time() - start_time} - {human_order}")
    chatbot.chat(human_order)
    return {"message": "Hello, this is the receive_audio endpoint!"}


@app.post("/receive_command")
def receive_command(
    human_order: str = Form(...), chatbot: OpenAIChatBot = Depends(get_chatbot)
):
    logger.debug(f"Processing: {human_order}")
    chatbot.chat(human_order)
    return {"message": "Hello, this is the receive_audio endpoint!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
