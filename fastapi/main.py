from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username : str
    age: int
    location : str


user_data = {
    "virat":{"username":"virat","age":30,"location":"Banglore"},
    "rohit":{"username":"rohit","age":32,"location":"mumbai"}
    }



@app.get("/")
def get_root():
    return {"output":"Welcome to the world"}

@app.get("/users")
def get_users():
    user_list = list(user_data.values())
    return user_list

@app.get("/users/{username}")
def get_user_info(username:str):
    return user_data[username]


@app.post("/users")
def post_user(user:User):
    username = user.username
    user_data[username] = user.dict()
    return {'message':f"successfully created user: {username}"}


@app.delete("/users/{username}")
def delete_user(username:str):
    del user_data[username]
    return {'message':f'Successfully Deleted user : {username}'}

@app.put('/users')
def update_user(user:User):
    username = user.username
    user_data[username] = user.dict()
    return {'message':f'Successfully updated user: {username}'}
