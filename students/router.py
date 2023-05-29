from fastapi import APIRouter
from .storage import get_students_list
from .schema import StudentCreateSchema, StudentUpdateSchema


router = APIRouter()

@router.get("/")
async def get_all_students():
    return get_students_list()

@router.post("/", status_code=200)
async def create_student(student: StudentCreateSchema):
    get_students_list().append(student)
    return student


@router.get("/{student_id}")
async def get_student(student_id: int):
    return get_students_list()[student_id]

@router.put("/{student_id}")
async def update_student(student_id: int,
                         student: StudentUpdateSchema):
    get_students_list()[student_id] = student
    return student

@router.delete("/{student_id}")
async def delete_student(student_id: int):
    return get_students_list().pop(student_id)