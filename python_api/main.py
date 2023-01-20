from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv
import os

from fastapi import FastAPI, Request
import openai
import json


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


openai.api_key = os.getenv('OPEN_AI_TOKEN_API')

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    text = data["text"]
    print(text)
    print("here")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=(f"{text}"),
        temperature=0.5,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return json.dumps(response["choices"][0]["text"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv('PUBLIC_FASTAPI_HOST'),
        port=int(os.getenv('PUBLIC_FASTAPI_PORT')),
        log_level="info",
        reload = bool(os.getenv('PUBLIC_FASTAPI_RELOAD'))
    )