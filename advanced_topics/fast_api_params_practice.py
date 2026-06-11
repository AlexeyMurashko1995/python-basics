from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

fake_bikes_db = [
    {"id": 1, "model": "Duotts C29", "type": "electric", "price": 4500},
    {"id": 2, "model": "Cargo X2", "type": "cargo", "price": 8200},
    {"id": 3, "model": "Duotts S26", "type": "electric", "price": 5200},
    {"id": 4, "model": "City E-Bike", "type": "city", "price": 3100},
    {"id": 5, "model": "Cargo Max", "type": "cargo", "price": 9500},
]

@app.get('/bikes')
def get_bikes(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=2, ge=1, le=4),
    type: str | None = None
):
    filtered_bikes = fake_bikes_db
    if type is not None:
        filtered_bikes = [bike for bike in filtered_bikes if bike['type'] == type]
    start = skip
    finish = skip + limit
    return filtered_bikes[start:finish]



