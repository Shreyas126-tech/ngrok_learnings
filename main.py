from fastapi import FastAPI
from routes.user_routes import router as user_router
from db import Base, engine
import models

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router, prefix="/api", tags=["Users"])
