
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/hello")
def read_hello():
    
    return JSONResponse({"message":"hello world"}ok, status_code=200,)
    

class WelcomeRequest(BaseModel):
    name: str



@app.get("/welcom")
def read_welcom(name: str = "Non défini"):
    return JSONResponse({"welcom"+name}ok, status_code=200,)





