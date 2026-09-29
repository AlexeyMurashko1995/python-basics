async def calculate_delivery_cost(cost: float, distance: int, add_cost):
    additional_cost = await add_cost(distance)
    return cost + additional_cost