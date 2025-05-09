from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session 
from app.db.dependencies import get_db
from app.db.models import User 
from app.db.database import Base, engine

router = APIRouter() 

Base.metadata.create_all(bind=engine)

@router.post("/users")
async def create_user(request: Request, db: Session = Depends(get_db)):
    payload = await request.json()
    name: str = payload['name']
    email: str = payload['email']
    where: str = payload['where']
    db.add(
        User(name=name, email=email, where=where)
    )
    db.commit()
    return {"message":"success"}, 200


@router.get("/users/{id}")
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id==id).first()
    return {
        "name": user.name, 
        "email": user.email,
        "where": user.where
    }

@router.get("/users")
async def get_user(db: Session = Depends(get_db)):
    users = db.query(User).all()
    data = []
    for row in users:
        data.append({
            "name": row.name, 
            "email": row.email,
            "where": row.where
        })
    return {"data": data}
