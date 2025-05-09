from fastapi import FastAPI, Depends 
from fastapi.middleware.cors import CORSMiddleware
from .db.dependencies import get_db
from .db.database import SessionLocal, Base, engine
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
from .utils.seed import seed_database
from .api.routes import router as api_router


@asynccontextmanager 
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    db: Session = SessionLocal()
    seed_database(db)
    db.close()
    yield 

app = FastAPI(lifespan=lifespan)

app.include_router(api_router, prefix="/api/v1", tags=["recipe"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)