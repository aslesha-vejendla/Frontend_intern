from fastapi import FastAPI

from app.database import Base, engine
from app.routes import auth, tasks

app = FastAPI(title="Fullstack Dashboard API")

# Create DB tables
Base.metadata.create_all(bind=engine)

# Routes
app.include_router(auth.router)
app.include_router(tasks.router)


@app.get("/")
def root():
    return {"message": "API running"}
