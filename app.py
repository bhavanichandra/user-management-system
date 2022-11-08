from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class PingResponse(BaseModel):
    status: bool
    message: str


@app.get("/", response_model=PingResponse)
def ping():
    """
        Ping the API to know its status
    """
    return {"status": True, "message": "API is Online!"}