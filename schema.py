from sqlalchemy import Column  , Integer , String  , Boolean
from sqlalchemy.orm import DeclarativeBase 

class Base(DeclarativeBase): 
    pass 

class Task(Base): 
    __tablename__ = "tasks" 
    id = Column(Integer , primary_key= True  ) 
    title = Column(String)
    description  = Column(String)
    is_completed = Column(Boolean , index = True ,default= False )
