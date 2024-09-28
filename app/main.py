from uvicorn import run
from api.app import app  # Import your FastAPI app

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)


