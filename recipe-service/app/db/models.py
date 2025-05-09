from .database import Base 
from sqlalchemy import Column, String, Integer, Float

class Recipe(Base):
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    calorie = Column(Integer, index=True)
    nutriscore = Column(Integer, index=True)
    rating = Column(String, index=True)
    voting = Column(Integer, index=True)
    tags = Column(String, index=True)
    image = Column(String, index=True)

