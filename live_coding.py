# # ---------- Task 1 ----------


# def get_word_lengths(words: list[str]) -> dict[str, int]:
#     clean_dict = {}
#     for word in words:
#         if len(word) > 0:
#             clean_dict[word] = len(word)
#     return clean_dict


# our_list = ["python", "fastapi", "", "sql", "python"]

# print(get_word_lengths(our_list))

# # ---------- Task 2 ----------


# def filter_users_by_age(users: list[dict], min_age: int) -> list[str]:
#     filtered_list = []
#     for user in users:
#         age = user.get("age")
#         name = user.get("name")

#         if age is not None and age >= min_age and name:
#             filtered_list.append(name)

#     return filtered_list


# users = [
#     {"name": "Alex", "age": 30},
#     {"name": "Bob", "age": 17},
#     {"name": "Eva", "age": 22},
#     {"name": "Unknown"}
# ]

# min_age = 18

# print(filter_users_by_age(users, min_age))

# # ---------- Task 3 ----------

# def filter_products_by_price(products: list[dict], max_price: float) -> list[str]:
#     filtered_list = []
#     for product in products:
#         title = product.get("title")
#         price = product.get("price")
#         is_available = product.get("is_available")
#         if title and price is not None and price <= max_price and is_available:
#             filtered_list.append(title)
#     return filtered_list

# products = [
#     {"title": "Laptop", "price": 1200.0, "is_available": True},
#     {"title": "Mouse", "price": 25.0, "is_available": True},
#     {"title": "Keyboard", "price": 80.0, "is_available": False},
#     {"title": "Monitor", "price": 300.0, "is_available": True},
#     {"price": 10.0, "is_available": True}
# ]
# max_price = 100.0

# print(filter_products_by_price(products, max_price))

# ---------- Task 4 ----------

def count_orders_by_status(orders: list[dict]) -> dict[str, int]:
    count_dict = {}
    for order in orders:
        status = order.get("status", "unknown")
        count_dict[status] = count_dict.get(status, 0) + 1

    return count_dict


orders = [
    {"id": 1, "status": "completed"},
    {"id": 2, "status": "pending"},
    {"id": 3, "status": "completed"},
    {"id": 4},
    {"id": 5, "status": "cancelled"}
]

print(count_orders_by_status(orders))