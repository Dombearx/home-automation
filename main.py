from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    from src.core.server.server import app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
