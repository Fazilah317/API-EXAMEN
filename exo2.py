from typing import List
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "Hello world",status code = 200}


@app.get("/welcome")
async def welcome(name: str):
    return {"message": f"Welcome {name}",status code =200}

class StudentModel(BaseModel):
    Reference: str
    FirstName: str
    LastName: str
    Age: int

students_store: List[StudentModel] = []


@app.post("/students", status_code=201)
async def create_students(students: List[StudentModel]):
    students_store.extend(students)
    return students_store


@app.get("/students")
async def get_students():
    return students_store


@app.put("/students")
async def update_or_create_student(student: StudentModel):
    for i, existing_student in enumerate(students_store):
        if existing_student.Reference == student.Reference:
            students_store[i] = student
            return students_store
    students_store.append(student)
    return students_store



@app.get("/students-authorized")
async def get_students_authorized(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    if authorization != "bon courage":
        raise HTTPException(status_code=403, detail="Invalid authorization credentials")
    return students_store
