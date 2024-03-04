
from src.application.webhook_controller import router as webhook_app
from fastapi import FastAPI
import uvicorn

app = FastAPI()

app.include_router(webhook_app)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)