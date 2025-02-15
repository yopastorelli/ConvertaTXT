from fastapi import FastAPI
from app import models, database
from app.api.api import router as api_router

app = FastAPI()

@app.on_event("startup")
async def startup():
    database.connect()

@app.on_event("shutdown")
async def shutdown():
    database.disconnect()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao ConvertaTXT"}

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
