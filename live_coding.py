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

# # ---------- Task 4 ----------

# def count_orders_by_status(orders: list[dict]) -> dict[str, int]:
#     count_dict = {}
#     for order in orders:
#         status = order.get("status", "unknown")
#         count_dict[status] = count_dict.get(status, 0) + 1

#     return count_dict


# orders = [
#     {"id": 1, "status": "completed"},
#     {"id": 2, "status": "pending"},
#     {"id": 3, "status": "completed"},
#     {"id": 4},
#     {"id": 5, "status": "cancelled"}
# ]

# print(count_orders_by_status(orders))

# # ---------- Task 5 ----------

# def count_logs_by_level(logs: list[dict]) -> dict[str, int]:
#     filtered_dict = {}
#     for log in logs:
#         level = log.get("level", "UNKNOWN")
#         filtered_dict[level] = filtered_dict.get(level, 0) + 1
#     return filtered_dict


# logs = [
#     {"level": "INFO", "message": "User logged in"},
#     {"level": "ERROR", "message": "Database connection failed"},
#     {"level": "INFO", "message": "Page loaded"},
#     {"message": "Cron job executed"},
#     {"level": "WARNING", "message": "High memory usage"}
# ]

# print(count_logs_by_level(logs))

# # ---------- Task 6 ----------

# def count_payment_method(payments: list[dict]) -> dict[str, int]:
#     count_payment = {}
#     for payment in payments:
#         method = payment.get("method", "unknown")
#         count_payment[method] = count_payment.get(method, 0) + 1
#     return count_payment


# payments = [
#     {"id": 1, "method": "card"},
#     {"id": 2, "method": "cash"},
#     {"id": 3, "method": "card"},
#     {"id": 4},
#     {"id": 5, "method": "crypto"}
# ]

# print(count_payment_method(payments))

# # ---------- Task 7 ----------

# def sum_payments_by_method(payments: list[dict]) -> dict[str, int]:
#     filtered_payments = {}
#     for payment in payments:
#         method = payment.get("method", "unknown")
#         amount = payment.get("amount", 0)
#         filtered_payments[method] = filtered_payments.get(method, 0) + amount
#     return filtered_payments

# payments = [
#     {"amount": 100, "method": "card"},
#     {"amount": 50, "method": "cash"},
#     {"amount": 200, "method": "card"},
#     {"amount": 30, "method": "cash"},
#     {"amount": 10}
# ]

# print(sum_payments_by_method(payments))

# # ---------- Task 8 ----------

# def sum_revenue_by_category(sales: list[dict]) -> dict[str, float]:
#     filtered_sales = {}
#     for sale in sales:
#         category = sale.get("category", "other")
#         price = sale.get("price")
#         filtered_sales[category] = filtered_sales.get(category, 0) + price
#     return filtered_sales


# sales = [
#     {"category": "electronics", "price": 200.0},
#     {"category": "books", "price": 15.0},
#     {"category": "electronics", "price": 50.0},
#     {"category": "books", "price": 10.0},
#     {"price": 5.0}
# ]

# print(sum_revenue_by_category(sales))

# # ---------- Task 9 ----------

# def sum_scores_by_player(results: list[dict]) -> dict[str, int]:
#     filtered_results = {}
#     for result in results:
#         player_name = result.get("player", "unknown")
#         score = result.get("score", 0)
#         filtered_results[player_name] = filtered_results.get(player_name, 0) + score
#     return filtered_results

# results = [
#     {"player": "Alex", "score": 10},
#     {"player": "Bob", "score": 5},
#     {"player": "Alex", "score": 15},
#     {"score": 20},
#     {"player": "Bob", "score": 10}
# ]

# print(sum_scores_by_player(results))

# ---------- Task 10 ----------

# def sum_duration_by_category(videos: list[dict]) -> dict[str, int]:
#     filtered_videos = {}
#     for video in videos:
#         category = video.get("category", "unknown")
#         duration = video.get("duration", 0)
#         filtered_videos[category] = filtered_videos.get(category, 0) + duration
#     return filtered_videos


# videos = [
#     {"category": "Python", "duration": 300},
#     {"category": "English", "duration": 120},
#     {"category": "Python", "duration": 450},
#     {"duration": 200},
#     {"category": "English", "duration": 180}
# ]

# print(sum_duration_by_category(videos))

# # ---------- Task 11 ----------

# def get_most_expensive_product(products: dict[str, float]) -> str:
#     max_price = 0.0
#     max_title = ""
#     for title, price in products.items():
#         if price >= max_price:
#             max_price = price
#             max_title = title
#     return (max_title)


# products = {
#     "Laptop": 1200.0,
#     "Mouse": 25.0,
#     "Monitor": 300.0
# }

# print(get_most_expensive_product(products))

# # ---------- Task 12 ----------

# def get_top_student(grades: dict[str, float]) -> str:
#     max_grade = 0.0
#     max_name = ""
#     for name, grade in grades.items():
#         if grade >= max_grade:
#             max_grade = grade
#             max_name = name
#     return max_name


# grades = {
#     "Alex": 4.5,
#     "Elena": 4.9,
#     "Petr": 3.8
# }

# print(get_top_student(grades))

# # ---------- Task 13 ----------

# def filter_high_scores(scores: dict[str, int], threshold: int) -> list[str]:
#     winner_list = []
#     for name, score in scores.items():
#         if score >= threshold:
#             winner_list.append(name)
#     return winner_list

# scores = {
#     "Alex": 85,
#     "Bob": 60,
#     "Eva": 92,
#     "Petr": 45
# }
# threshold = 80

# print(filter_high_scores(scores, threshold))

# # ---------- Task 14 ----------

# def check_reorder_needed(stock: dict[str, int], thresholds: dict[str, int]) -> list[str]:
#     filtered_products_list = []
#     for item, count in stock.items():
#         threshold = thresholds.get(item, 10)
#         if count < threshold:
#             filtered_products_list.append(item)
#     return filtered_products_list

# stock = {
#     "Laptop": 3,
#     "Mouse": 15,
#     "Keyboard": 2,
#     "Monitor": 12
# }

# thresholds = {
#     "Laptop": 5,
#     "Mouse": 10
# }

# print(check_reorder_needed(stock, thresholds))

# # ---------- Task 15 ----------

# def apply_discounts(prices: dict[str, float], discounts: dict[str, float]) -> dict[str, float]:
#     final_prices = {}
#     for name, price in prices.items():
#         discount = discounts.get(name, 0)
#         final_prices[name] = price - discount
#     return final_prices

# prices = {
#     "Laptop": 1000.0,
#     "Mouse": 25.0,
#     "Monitor": 200.0
# }

# discounts = {
#     "Laptop": 100.0,
#     "Mouse": 5.0
# }

# print(apply_discounts(prices, discounts))

# # ---------- Task 16 ----------

# def calculate_item_totals(quantities: dict[str, int], prices: dict[str, float]) -> dict[str, float]:
#     final_data = {}
#     for name, quantity in quantities.items():
#         price = prices.get(name, 0.0)
#         final_data[name] = price * quantity
#     return final_data


# quantities = {
#     "Laptop": 2,
#     "Mouse": 5,
#     "Keyboard": 1
# }

# prices = {
#     "Laptop": 1000.0,
#     "Mouse": 25.0
# }

# print(calculate_item_totals(quantities, prices))

# ---------- Task 17 ----------

def calculate_final_scores(scores: dict[str, int], bonuses: dict[str, int]) -> dict[str, int]:
    final_scores = {}
    for student, score in scores.items():
        bonus = bonuses.get(student, 0)
        final_scores[student]= score + bonus
    return final_scores

scores = {
    "Alex": 80,
    "Bob": 75,
    "Eva": 90
}

bonuses = {
    "Alex": 10,
    "Eva": 5
}

print(calculate_final_scores(scores, bonuses))