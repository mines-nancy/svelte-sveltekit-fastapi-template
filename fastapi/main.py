from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

## CORS SECURITY
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
        "http://localhost:5173",
        "http://localhost:4173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
