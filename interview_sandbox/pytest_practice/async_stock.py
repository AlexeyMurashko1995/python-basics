async def get_product_in_stock(product_id: int) -> bool:
    return True


async def get_product_price(product_id: int) -> int:
    in_stock = await get_product_in_stock(product_id)
    if in_stock:
        return 20
    raise ValueError("Product is not found")