from fastapi import FastAPI
from database import engine, Base
import models, routes

# Auto-create table in MySQL 
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mynder User API")
app.include_router(routes.router)