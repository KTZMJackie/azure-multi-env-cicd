import os
from fastapi import FastAPI

app = FastAPI()

ENV_NAME = os.getenv("APP_ENV", "unknown")

@app.get("/")
def root():
    return {
        "message": "Hello from Azure Multi-Environment CI/CD Project",
        "environment": ENV_NAME
    }

@app.get("/health")
def health():
    return {"status": "healthy", "environment": ENV_NAME}