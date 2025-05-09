from fastapi import FastAPI 
from app.api.routes import router as api_router 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() 

app.include_router(api_router, prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True,
    allow_origins=["*"]
)