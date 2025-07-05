from fastapi import FastAPI , Depends , HTTPException 
from sqlalchemy.orm import Session 

from schema import Task , Base 

from models import  TaskModel , CreateTaskModel , EditTaskModel

from database import SessionLocal , engine 

Base.metadata.create_all(bind=engine) 

app = FastAPI() 

def get_db():
    db = SessionLocal() 
    try: 
        yield db 
    finally: 
        db.close() 


@app.post("/tasks" ,  response_model= TaskModel ) 
def create_task( task:CreateTaskModel ,  db: Session = Depends(get_db)): 
    newTask = Task(title = task.title , description = task.description) 
    db.add(newTask) 
    db.commit() 
    db.refresh(newTask)
    return newTask 


@app.get("/tasks" , response_model= list[TaskModel] )
def get_tasks( is_completed:bool | None = None  ,  db:Session = Depends(get_db)):
    if is_completed is None:
        return  db.query(Task).all() 
    else :
        return  db.query(Task).filter(Task.is_completed==is_completed)   

@app.get("/tasks/{id}", response_model=TaskModel)
def get_task(id: int,  db:Session= Depends(get_db)):
    task = db.query(Task).filter( Task.id == id).first()  
    if not task: 
        raise HTTPException(status_code=404,detail="Task not found")
    return task 

@app.put("/tasks/{id}") 
def edit_task(id:int , task : EditTaskModel ,  db:Session = Depends(get_db)):
    existingTask = db.query(Task).filter(id == Task.id).first()
    if not existingTask: 
        raise HTTPException(status_code=404 , detail= "Task not found.")
    if task.title  is not None: 
        existingTask.title = task.title 
    if task.description is  not None: 
        existingTask.description = task.description 
    if task.is_completed is  not None:
        existingTask.is_completed = task.is_completed
    db.commit() 
    db.refresh(existingTask)
    return  existingTask

@app.delete("/tasks/{id}") 
def delete_task(id:int ,  db:Session = Depends(get_db) ): 
    task = db.query(Task).filter(id==Task.id).first() 
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit() 
    



    




