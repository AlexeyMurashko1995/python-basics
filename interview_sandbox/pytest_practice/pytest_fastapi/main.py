from fastapi import Depends, FastAPI


app = FastAPI()


async def get_current_user():
    return {"role": "guest"}


@app.get("/api/v1/profile")
async def get_profile(user = Depends(get_current_user)):
    return {"user": user}