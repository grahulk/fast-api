from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI

from model import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("ced388f0-d5f0-4d13-a60a-d5b4a996a8e7"),
        first_name="Selena",
        last_name="Gomez",
        gender=Gender.female,
        roles=[Role.admin]
    ),
    User(
        id=UUID("e4a77538-c5c2-4e13-a1a5-bc34b5641d75"),
        first_name="Vishnu",
        last_name="Viswambharan",
        gender=Gender.male,
        roles=[Role.user]
    )
]


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


# @app.delete("/apiv1/delete_users")
# async def remove_users(userid : str):
#     db.remove
