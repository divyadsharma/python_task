from fastapi import FastAPI
from .database import engine, Base
from .controllers import task_controller

# engine is required to create tables from models (Base.metadata.create_all(bind=engine)).
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(task_controller.router)

@app.get("/")
def root():
    return {"message": "Task Manager API is running 🚀"}