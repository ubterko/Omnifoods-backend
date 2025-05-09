from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from ..db.dependencies import get_db 
from ..db.models import Recipe 

router = APIRouter() 

@router.get("/recipes")
def get_recipe(db: Session = Depends(get_db)):
    result = db.query(Recipe).all() 
    return result 

    

