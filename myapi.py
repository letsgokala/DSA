from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "john",
        "age": 17,
        "year": "year 12"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str
    
class UpdateStudent(BaseModel):
    name : Optional[str] = None,
    age : Optional[int] = None,
    year : Optional[str] = None

@app.get("/")
def index():
    return {"name": "khalid muzemil"}

@app.get("/get-students")
def get_students():
    return students

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="enter a number", gt=0, lt=5)):
    for stu_id in students:
        print(stu_id)
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student_by_name(*, student_id, name: Optional[str] = None, test : int):
    # We can't make a normal argument after a default argument but if we use the * as the first parameter it possible
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        
    return {"Data" : "Data Not Found"}

@app.post("/create-student/{student_id}")
def createstudent(student_id : int, student : Student):
    if student_id in students:
        return {"error": "student exists"}
        
    students[student_id] = student.model_dump()
    return students

@app.put("/update-student/{student_id}")
def update_student(student_id : int, student : UpdateStudent):
    if student_id not in students:
        return {"error" : "studnet was not found"}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age
        
    if student.year != None:
        students[student_id].year = student.year        
        
    return students[student_id]