async def calculate_total_with_tax(product_price: float, country_code: str, tax_func):
    tax = await tax_func(country_code)
    return product_price + (product_price * tax / 100)