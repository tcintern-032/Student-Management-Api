from fastapi import FastAPI, HTTPException, status
from models import Student, StudentCreate
app = FastAPI(
    title="Student Management API",
    description="Simple Student Management System using FastAPI",
    version="1.0"
)
students = [
    {
        "id": 1,
        "name": "Ali",
        "age": 20,
        "course": "Computer Science"
    },
    {
        "id": 2,
        "name": "Ahmed",
        "age": 22,
        "course": "Information Technology"
    },
     {
        "id": 3,
        "name": "Nasir",
        "age": 21,
        "course": "Data Science"
    },
     {
        "id": 4,
        "name": "Arbab",
        "age": 22,
        "course": "Software Enginering"
    },
     {
        "id": 5,
        "name": "Faisal",
        "age": 23,
        "course": "Accounting & Finance"
    },
     {
        "id": 6,
        "name": "Asad",
        "age": 23,
        "course": "English"
    }
]
# Home Route
@app.get("/")
def home():
    return {
        "message": "Welcome to Student Management API"
    }
# GET All Students
@app.get("/students", response_model=list[Student])
def get_students():
    return students
# GET Student By ID
@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )
# POST New Student
@app.post(
    "/students",
    response_model=Student,
    status_code=status.HTTP_201_CREATED
)
def add_student(student: StudentCreate):
    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }
    students.append(new_student)
    return new_student
# PUT Update Student
@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, updated_student: StudentCreate):
    for student in students:
        if student["id"] == student_id:      
            student["name"] = updated_student.name
            student["age"] = updated_student.age
            student["course"] = updated_student.course
            return student
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )
# DELETE Student
@app.delete(
    "/students/{student_id}",
    status_code=status.HTTP_200_OK
)
def delete_student(student_id: int):
    for student in students:
       if student["id"] == student_id:
            students.remove(student)
            return {
                "message": "Student deleted successfully"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )