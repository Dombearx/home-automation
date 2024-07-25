import logging

from fastapi import FastAPI, Form, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from functions import YoutubeConnector

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    exc_str = f"{exc}".replace("\n", " ").replace("   ", " ")
    logging.error(f"{request}: {exc_str}")
    content = {"status_code": 10422, "message": exc_str, "data": None}
    return JSONResponse(
        content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )


@app.post("/play_video")
def receive_command(request: Request, url: str = Form(...)):
    YoutubeConnector.play_video(url)
    return {"response": "OK"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
