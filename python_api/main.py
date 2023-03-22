from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv
import os
import csv

from fastapi import FastAPI, Request



if os.getenv('ENV_MODE') == 'development':
    load_dotenv("scripts/dev/.env")
else:
    load_dotenv("scripts/prod/.env")


app = FastAPI()

allow_origins = [
        os.getenv('PUBLIC_SVELTEKIT_URL'),
        os.getenv('PUBLIC_FASTAPI_URL')
    ]

print(allow_origins)
## CORS SECURITY
app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class TimerData(BaseModel):
    task: str
    hours: int
    minutes: int
    seconds: int
    milliseconds: int


@app.post("/save_timer")
async def save_timer(data: TimerData):
    with open("static/public/times.csv", "a") as file:
        writer = csv.writer(file, delimiter=';')  # Utiliser le point-virgule comme séparateur
        writer.writerow([data.task, data.hours, data.minutes, data.seconds, data.milliseconds])

    return {"status": "success"}



if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv('PUBLIC_FASTAPI_HOST'),
        port=int(os.getenv('PUBLIC_FASTAPI_PORT')),
        log_level="info",
        reload = bool(os.getenv('PUBLIC_FASTAPI_RELOAD'))
    )