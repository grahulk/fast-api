from typing import List
from uuid import uuid4
from fastapi import FastAPI

from model import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Selena",
        last_name="Gomez",
        gender=Gender.female,
        roles=[Role.admin]
    ),
    User(
        id=uuid4(),
        first_name="Vishnu",
        last_name="Viswambharan",
        gender=Gender.male,
        roles=[Role.user]
    )
]


@app.get("/")
async def root():
    return {"Hello": "World"}
