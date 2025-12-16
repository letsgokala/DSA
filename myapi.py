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
