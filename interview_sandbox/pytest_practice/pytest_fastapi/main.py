from fastapi import FastAPI


app = FastAPI()


@app.get("/health")
async def get_dict():
    return {"status": "ok"}