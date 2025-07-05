from pydantic import BaseModel 

class TaskModel(BaseModel): 
    id : int  
    title : str 
    description : str 
    is_completed : bool 

class CreateTaskModel(BaseModel): 
    title: str 
    description: str 

class EditTaskModel(BaseModel): 
    title: str | None  = None 
    description: str | None   = None 
    is_completed: bool | None  = None 
