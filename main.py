from typing import List
from fastapi import FastAPI

from model import User

app = FastAPI()

db: List[User] = [

]


@app.get("/")
async def root():
    return {"Hello": "World"}
