from fastapi import FastAPI

app = FastAPI()

fake_parcels_db = [
    {"id": 1, "tracking_number": "POL-1001", "category": "electronics", "weight": 1.5},
    {"id": 2, "tracking_number": "POL-1002", "category": "clothes", "weight": 0.8},
    {"id": 3, "tracking_number": "POL-1003", "category": "electronics", "weight": 12.4},
    {"id": 4, "tracking_number": "POL-1004", "category": "books", "weight": 2.1},
    {"id": 5, "tracking_number": "POL-1005", "category": "clothes", "weight": 1.1},
    {"id": 6, "tracking_number": "POL-1006", "category": "electronics", "weight": 5.0},
    {"id": 7, "tracking_number": "POL-1007", "category": "books", "weight": 0.5},
]

@app.get('/parcels')
def get_parcels(skip: int | None = 0, limit: int | None = 3, category: str | None = None):
    filtered_parcels = fake_parcels_db
    if category is not None:
        filtered_parcels = [p for p in filtered_parcels if p['category'] == category]
    start = skip
    end = skip + limit
    return filtered_parcels[start:end]
