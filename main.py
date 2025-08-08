from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/my")
def read_root():
    return {"message": "Hello from vighnesh!"}



# RUN THIS FILE
#  uvicorn app.main:app --reload
