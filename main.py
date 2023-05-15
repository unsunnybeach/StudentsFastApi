from fastapi import FastAPI
from pydantic import BaseModel

class StudentCreateSchema(BaseModel):
    first_name: str
    last: str

class StudentUpdateSchema(BaseModel):
    first_name: str
    last_name: str

app = FastAPI()

students = [{"first_name": "str",
         "last_name": "str"
         }]


@app.get("/students/")
async def get_all_students():
    return students

@app.post("/students/", status_code=200)
async def create_student(student: StudentCreateSchema):
    students.append(student)
    return student


@app.get("/student/{student_id}")
async def get_student(student_id: int):
    return students[student_id]

@app.put("/student/{student_id}")
async def update_student(student_id: int,
                         student: StudentUpdateSchema):
    students[student_id] = student
    return student
