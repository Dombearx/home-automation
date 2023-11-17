import logging
from io import BytesIO

from fastapi import FastAPI, File, Request, UploadFile, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from loguru import logger

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


@app.get("/")
def read_root():
    return {"message": "Hello, this is the root endpoint!"}


@app.post("/receive_audio")
def receive_audio(audioFile: UploadFile = File(...)):
    recognize(audioFile)
    return {"message": "Hello, this is the receive_audio endpoint!"}
    #
    #     os.system("ffmpeg -y -i tmp_filename.3gp tmp_filename.wav")
    #     print("Start file processing", file=sys.stderr)
    #     recognize()
    #     return "Audio received successfully"
    # except Exception as e:
    #     print(f"Error: {e}")
    #
    #     return "Error receiving audio", 500


def recognize(audio_data):
    # model_name = "gpt-3.5-turbo"
    # chatbot = OpenAIChatBot(model_name)
    recognition = SpeechRecognition()
    human_order = recognition.recognize_from_file(BytesIO(audio_data.file.read()))
    logger.debug(human_order)
    # chatbot.chat(human_order)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
