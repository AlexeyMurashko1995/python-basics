def get_distance(city: str) -> float:
    return 100


def calculate_shipping(city: str, weight: float) -> float:
    distance = get_distance(city)
    return weight * distance