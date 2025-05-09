from app.db.database import Base 
from sqlalchemy import String, Column, Integer 

class User(Base):
    __tablename__ = "user" 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True) 
    where = Column(String, index=True)
