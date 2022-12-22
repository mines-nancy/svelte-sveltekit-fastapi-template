from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv
import os


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
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/helloworld")
async def helloword0(name: Union[str, None] = None, name2: Union[str, None] = None):
    return {"HelloWorld": name2+name}

@app.get("/helloworld/{name}")
async def helloword1(name:str):
    return {"HelloWorld": name}


class Person(BaseModel):
    name: str
    age: int
    address: Union[str, None] = None

@app.post("/helloworld")
async def helloword2(person: Person):
    return {"HelloWorld": person.name + " " + str(person.age)}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv('PUBLIC_FASTAPI_HOST'),
        port=int(os.getenv('PUBLIC_FASTAPI_PORT')),
        log_level="info",
        reload = bool(os.getenv('PUBLIC_FASTAPI_RELOAD'))
    )