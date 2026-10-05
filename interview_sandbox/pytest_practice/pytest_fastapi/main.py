from fastapi import FastAPI, Depends, HTTPException


app = FastAPI()


async def get_api_key():
    return "invalid_key"


@app.get("/api/v1/secret_data")
async def get_data(key=Depends(get_api_key)):
    if key != "valid_key":
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return {"data": "top_secret_payload"}