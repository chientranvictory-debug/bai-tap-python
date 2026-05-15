from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
  name: str
  age: int

app = FastAPI()

@app.get("/")
def read_root():
 return {"message": "Hello World"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
   return {"user_id": user_id, "name": f"User {user_id}"}


@app.post("/users")
def create_user(user: User):
 return {"created": user}

if __name__ == "__main__":
 import uvicorn
 uvicorn.run(app, host="0.0.0.0", port=8000)