from fastapi import FastAPI
from users import users

app = FastAPI()

# Root Route
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API!"}  

# GET REQUEST
@app.get("/users")
def get_users():
    return {"users": users}

# GET REQUEST by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return {"user": user}
    return {"error": "User not found"}, 404

# POST REQUEST
@app.post("/users")
def add_user(user: dict):
    user["id"] = len(users) + 1
    users.append(user)
    return {"user": user}, 201