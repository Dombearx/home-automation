import logging
import time
from contextlib import asynccontextmanager
from io import BytesIO

from fastapi import FastAPI, File, Form, Request, UploadFile, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from loguru import logger

from src.core.assistant.open_ai_assistatnt import OpenAIChatBot
from src.core.voice_recognition.voice_recognition import SpeechRecognition


def load_chatbot():
    model_name = "gpt-3.5-turbo"
    temperature = 0.7
    return OpenAIChatBot(model_name, temperature)


def load_recognition():
    recognition = SpeechRecognition("medium")
    return recognition


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Run at startup
    Initialise the Client and add it to request.state
    """
    chatbot = load_chatbot()
    recognition = load_recognition()
    yield {"chatbot": chatbot, "recognition": recognition}


app = FastAPI(lifespan=lifespan)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    exc_str = f"{exc}".replace("\n", " ").replace("   ", " ")
    logging.error(f"{request}: {exc_str}")
    content = {"status_code": 10422, "message": exc_str, "data": None}
    return JSONResponse(
        content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )


@app.get("/")
def read_root():
    return {"message": "Hello, this is the root endpoint!"}


@app.post("/receive_audio")
def receive_audio(request: Request, audioFile: UploadFile = File(...)):
    logger.debug(f"Processing audio file: {audioFile.filename}")
    start_time = time.time()
    human_order = request.state.recognition.recognize_from_file(
        BytesIO(audioFile.file.read())
    )
    logger.debug(f"Audio processed in {time.time() - start_time} - {human_order}")
    response = request.state.chatbot.chat(human_order)
    return {"response": response, "human_order": human_order}


@app.post("/receive_command")
def receive_command(request: Request, human_order: str = Form(...)):
    # mock response
    # return {"response": "I am a mock response"}
    logger.debug(f"Processing: {human_order}")
    response = request.state.chatbot.chat(human_order)
    return {"response": response}
