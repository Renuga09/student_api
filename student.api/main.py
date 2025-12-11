from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    course: str

students = []

@app.get("/")
def home():
    return {"message": "Welcome to Student API"}

@app.post("/students")
def create_student(student: Student):
    for s in students:
        if s.id == student.id:
            raise HTTPException(status_code=400, detail="ID already exists")
    students.append(student)
    return {"message": "Student Added", "student": student}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for s in students:
        if s.id == student_id:
            return s
    raise HTTPException(status_code=404, detail="Student not found")

@app.put("/students/{student_id}")
def update_student(student_id: int, new_student: Student):
    for index, s in enumerate(students):
        if s.id == student_id:
            students[index] = new_student
            return {"message": "Student Updated", "student": new_student}
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for s in students:
        if s.id == student_id:
            students.remove(s)
            return {"message": "Student Deleted"}
    raise HTTPException(status_code=404, detail="student removed")
