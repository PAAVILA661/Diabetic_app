from fastapi import FastAPI
from api.endpoints import router

app = FastAPI()

app.include_router(router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Diabetic Health Monitoring API"}