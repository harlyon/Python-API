from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    description: str
    location: str
    
class UpdateStudent(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None

students = {
    1: {
        "id": 1,
        "name": "Amos",
        "description": "Fully qualified student who has experience",
        "location": "Johannesburg",
    },
    2: {
        "id": 2,
        "name": "Beatrice",
        "description": "Home qualified student who has experience",
        "location": "Germany",
    },
   3: {
        "id": 3,
        "name": "Imtiyaaz",
        "description": "Technical student who has experience",
        "location": "Mumbai",
    },
    4:{
        "id": 4,
        "name": "Jabu",
        "description": "Leader who has experience and has experience with leading students",
        "location": "Harare",
    }
    
}

# GET ALL STUDENTS
@app.get('/')
def index():
    return students

# GET STUDENT BY ID
@app.get('/student/{id}')
def get_student(id: int = Path(None, description="ID of student you want to view")):
    return students[id];

# GET STUDENT BY NAME
@app.get('/student/name')
def get_student(name: Optional[str] = None):
    for id in students:
        if students[id]['name'] == name:
            return students[id]
        
        return {'Data': 'Not Found'};
    
#CREATE NEW STUDENT
@app.post('/create-students/{id}')
def create_students(id: int, student: Student):
    if id in students:
        return {'Error': 'Student already exists.'};
    
    students[id] = student;
    return students[id];

#UPDATE STUDENT BY ID
@app.post('/update-students/{id}')
def update_students(id: int, student: UpdateStudent):
    if id not in students:
        return {'Error': 'Student not found.'};
    
    if student.id != None:
      students[id].id = student.id;
      
    if students.name != None:
        students[id].name = student.name;
        
    if students.description != None:
        students[id].description = student.description;
        
    if students.location != None:
        students[id].location = student.location;
        
    return students[id];

#DELETE STUDENT RECORD BY ID
@app.delete('/delete-students/{id}')
def delete_students(id: int):
    if id not in students:
        return {'Error': 'Students not found.'};
    
    del students[id];
    return {'Message': 'Student record deleted.'};