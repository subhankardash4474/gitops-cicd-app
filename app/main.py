from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "This is a FastAPI Demo Project"}

@app.get("/health")
async def health_check():
    return {"status": "live"}

@app.get("/ready")
async def ready():
    return {"status": "ready"}

@app.get("/version")
async def version():
    return {"version": "0.1.0"}
