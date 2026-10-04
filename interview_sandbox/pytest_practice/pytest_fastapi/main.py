from fastapi import FastAPI


app = FastAPI()


@app.get("/health")
async def get_dict():
    return {"status": "ok"}


@app.get("/version")
async def get_version():
    return {"version": "1.0.0"}


@app.get("/api/v1/status")
async def get_status():
    return {"service": "auth_service", "online": True}