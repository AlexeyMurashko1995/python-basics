async def get_cargo_final_price(weight: float, country_id: int, get_coeff) -> float:
    coeff = await get_coeff(country_id)
    if coeff == "LOCAL":
        return weight * 10 * 1
    elif coeff == "EU":
        return weight * 10 * 1.5
    else:
        return weight * 10 * 2