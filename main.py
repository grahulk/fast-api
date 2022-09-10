from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

from model import Gender, Role, User, UserEdit

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


@app.delete("/app/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if(user.id == user_id):
            db.remove(user)
            return

    raise HTTPException(
        status_code=404,
        detail=f"User with id : {user_id} doesnt exist"
    )


@app.put("/api/v1/user/{user_id}")
async def edit_user(edituser: UserEdit, userid: UUID):
    for user in db:
        if(user.id == userid):
            if edituser.first_name is not None:
                user.first_name = edituser.first_name
            if edituser.last_name is not None:
                user.last_name = edituser.last_name
            if edituser.middle_name is not None:
                user.middle_name = edituser.middle_name
            if edituser.roles is not None:
                user.roles = edituser.roles

            return
    raise HTTPException(
        status_code=404,
        detail=f"User with id : {userid} doesnt exist"
    )
# i should fetch data from data base in fast api and dump it to angular front,
# mainly, get, post, put , delete and also host them.