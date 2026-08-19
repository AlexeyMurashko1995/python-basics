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

# # ---------- Task 17 ----------

# def calculate_final_scores(scores: dict[str, int], bonuses: dict[str, int]) -> dict[str, int]:
#     final_scores = {}
#     for student, score in scores.items():
#         bonus = bonuses.get(student, 0)
#         final_scores[student]= score + bonus
#     return final_scores

# scores = {
#     "Alex": 80,
#     "Bob": 75,
#     "Eva": 90
# }

# bonuses = {
#     "Alex": 10,
#     "Eva": 5
# }

# print(calculate_final_scores(scores, bonuses))

# # ---------- Task 18 ----------

# def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
#     result = {}
#     for word in words:
#         letter = word[0]
#         if letter not in result:
#             result[letter] = []
#         result[letter].append(word)
#     return result

# words = ["apple", "banana", "apricot", "blueberry", "car"]

# print(group_by_first_letter(words))

# # ---------- Task 19 ----------

# def group_employees_by_department(employees: list[dict]) -> dict[str, list[str]]:
#     department_list = {}
#     for employee in employees:
#         name = employee.get("name")
#         dep = employee.get("department")
#         if dep not in department_list:
#             department_list[dep] = []
#         department_list[dep].append(name)
#     return department_list

# employees = [
#     {"name": "Alex", "department": "IT"},
#     {"name": "Bob", "department": "HR"},
#     {"name": "Eva", "department": "IT"},
#     {"name": "Dan", "department": "Finance"}
# ]

# print(group_employees_by_department(employees))

# # ---------- Task 20 ----------

# def group_order_ids_by_status(orders: list[dict]) -> dict[str, list[int]]:
#     orders_stat = {}
#     for order in orders:
#         status = order.get("status")
#         id = order.get("id")
#         if status not in orders_stat:
#             orders_stat[status] = []
#         orders_stat[status].append(id)
#     return orders_stat

# orders = [
#     {"id": 101, "status": "completed"},
#     {"id": 102, "status": "pending"},
#     {"id": 103, "status": "completed"},
#     {"id": 104, "status": "cancelled"},
#     {"id": 105, "status": "pending"}
# ]

# print(group_order_ids_by_status(orders))

# # ---------- Task 21 ----------

# def group_students_by_grade(students: list[dict]) -> dict[str, list[str]]:
#     students_by_class = {}
#     for student in students:
#         name = student.get("name")
#         grade = student.get("grade")
#         if grade not in students_by_class:
#             students_by_class[grade] = []
#         students_by_class[grade].append(name)
#     return students_by_class


# students = [
#     {"name": "Alice", "grade": "5A"},
#     {"name": "Bob", "grade": "5B"},
#     {"name": "Charlie", "grade": "5A"},
#     {"name": "David", "grade": "5C"},
#     {"name": "Eva", "grade": "5B"}
# ]

# print(group_students_by_grade(students))

# # ---------- Task 22 ----------

# def group_by_author(books: list[dict]) -> dict[str, list[str]]:
#     author_books = {}
#     for book in books:
#         title = book.get("title")
#         author = book.get("author")
#         if author not in author_books:
#             author_books[author] = []
#         author_books[author].append(title)
#     return author_books

# books = [
#     {"title": "Dune", "author": "Frank Herbert"},
#     {"title": "1984", "author": "George Orwell"},
#     {"title": "Dune Messiah", "author": "Frank Herbert"},
#     {"title": "Animal Farm", "author": "George Orwell"},
#     {"title": "The Hobbit", "author": "J.R.R. Tolkien"}
# ]

# print(group_by_author(books))

# # ---------- Task 23 ----------

# def group_movies_by_genre(movies: list[dict]) -> dict[str, list[str]]:
#     sorted_movies = {}
#     for movie in movies:
#         title = movie.get("title")
#         genre = movie.get("genre")
#         if genre not in sorted_movies:
#             sorted_movies[genre] = []
#         sorted_movies[genre].append(title)
#     return sorted_movies

# movies = [
#     {"title": "Inception", "genre": "Sci-Fi"},
#     {"title": "The Godfather", "genre": "Crime"},
#     {"title": "Interstellar", "genre": "Sci-Fi"},
#     {"title": "Pulp Fiction", "genre": "Crime"},
#     {"title": "The Dark Knight", "genre": "Action"}
# ]

# print(group_movies_by_genre(movies))

# # ---------- Task 24 ----------

# def group_events_by_city(events: list[dict]) -> dict[str, list[str]]:
#     sorted_events = {}
#     for event in events:
#         name = event.get("name")
#         city = event.get("city")
#         if city not in sorted_events:
#             sorted_events[city] = []
#         sorted_events[city].append(name)
#     return sorted_events


# events = [
#     {"name": "Tech Conference", "city": "Warsaw"},
#     {"name": "Music Festival", "city": "Krakow"},
#     {"name": "AI Meetup", "city": "Warsaw"},
#     {"name": "Art Exhibition", "city": "Gdansk"},
#     {"name": "Backend Summit", "city": "Krakow"}
# ]

# print(group_events_by_city(events))

# # ---------- Task 25 ----------

# def group_users_by_age(users: list[dict]) -> dict[str, list[str]]:
#     sorted_users = {}
#     sorted_users["adult"] = []
#     sorted_users["minor"] = []
#     for user in users:
#         name = user.get("name")
#         age = user.get("age")
#         if age >= 18:
#             sorted_users["adult"].append(name)
#         else:
#             sorted_users["minor"].append(name)
#     return sorted_users


# users = [
#     {"name": "Alex", "age": 25},
#     {"name": "Bob", "age": 15},
#     {"name": "Eva", "age": 30},
#     {"name": "Dan", "age": 12}
# ]

# print(group_users_by_age(users))

# # ---------- Task 26 ----------

# def group_by_price_category(products: list[dict], threshold: float) -> dict[str,list[str]]:
#     sorted_products = {"expensive": [], "cheap": []}
#     for product in products:
#         title = product.get("title")
#         price = product.get("price")
#         if price >= threshold:
#             sorted_products["expensive"].append(title)
#         else:
#             sorted_products["cheap"].append(title)
#     return sorted_products

# products = [
#     {"title": "Laptop", "price": 1200.0},
#     {"title": "Mouse", "price": 25.0},
#     {"title": "Monitor", "price": 300.0},
#     {"title": "Cable", "price": 10.0}
# ]
# threshold = 100.0

# print(group_by_price_category(products, threshold))

# # ---------- Task 27 ----------

# def group_tasks_by_priority(tasks: list[dict]) -> dict[str, list[str]]:
#     sorted_tasks = {"urgent": [], "regular": []}
#     for task in tasks:
#         title = task.get("title")
#         is_urgent = task.get("is_urgent")
#         if is_urgent:
#             sorted_tasks["urgent"].append(title)
#         else:
#             sorted_tasks["regular"].append(title)
#     return sorted_tasks


# tasks = [
#     {"title": "Fix bug", "is_urgent": True},
#     {"title": "Write docs", "is_urgent": False},
#     {"title": "Deploy update", "is_urgent": True},
#     {"title": "Clean logs", "is_urgent": False}
# ]

# print(group_tasks_by_priority(tasks))

# # ---------- Task 28 ----------

# def invert_students_courses(student_courses: dict[str, str]) -> dict[str,list[str]]:
#     invert_students = {}
#     for student, course in student_courses.items():
#         if course not in invert_students:
#             invert_students[course] = []
#         invert_students[course].append(student)
#     return invert_students

# student_courses = {
#     "Alex": "Python",
#     "Bob": "JavaScript",
#     "Charlie": "Python",
#     "David": "C++",
#     "Eva": "JavaScript"
# }

# print(invert_students_courses(student_courses))

# # ---------- Task 29 ----------

# def invert_employee_roles(employee_roles: dict[str, str]) -> dict[str, list[str]]:
#     employee_department = {}
#     for name, department in employee_roles.items():
#         if department not in employee_department:
#             employee_department[department] = []
#         employee_department[department].append(name)
#     return employee_department

# employee_roles = {
#     "Alex": "Backend",
#     "Bob": "Frontend",
#     "Charlie": "Backend",
#     "David": "QA",
#     "Eva": "DevOps",
#     "Frank": "Frontend"
# }

# print(invert_employee_roles(employee_roles))

# # ---------- Task 30 ----------

# def find_duplicates(emails: list[str]) -> list[str]:
#     seen = set()
#     duplicates = set()
#     for email in emails:
#         if email not in seen:
#             seen.add(email)
#         else:
#             duplicates.add(email)
#     return list(duplicates)

# emails = [
#     "alex@gmail.com",
#     "bob@yahoo.com",
#     "alex@gmail.com",
#     "eva@hotmail.com",
#     "bob@yahoo.com",
#     "john@gmail.com"
# ]

# print(find_duplicates(emails))

# # ---------- Task 31 ----------

# def find_common_elements(list1: list[str], list2: list[str]) -> list[str]:
#     return list(set(list1) & set(list2))

# list1 = ["alex", "bob", "charlie", "david"]
# list2 = ["eva", "bob", "david", "frank"]

# print(find_common_elements(list1, list2))

# # ---------- Task 32 ----------

# def find_unique_to_first(list1: list[str], list2: list[str]) -> list[str]:
#     return list(set(list1) - set(list2))

# list1 = ["apple", "banana", "cherry", "date"]
# list2 = ["banana", "date", "fig"]

# print(find_unique_to_first(list1, list2))

# # ---------- Task 33 ----------

# def find_unique_in_either(list1: list[str], list2: list[str]) -> list[str]:
#     return list(set(list1) ^ set(list2))

# list1 = ["apple", "banana", "cherry"]
# list2 = ["banana", "date", "cherry"]

# print(find_unique_in_either(list1, list2))

# # ---------- Task 34 ----------

# def get_inactive_users(day1: list[str], day2: list[str]) -> list[str]:
#     return list(set(day1) - set(day2))

# day1 = ["alex", "bob", "eva", "john"]
# day2 = ["bob", "john", "marta"]

# print(get_inactive_users(day1, day2))

# # ---------- Task 35 ----------

# def get_unique_skills(dev1: list[str], dev2: list[str]) -> list[str]:
#     return list(set(dev1) ^ set(dev2))

# dev1 = ["python", "docker", "postgres"]
# dev2 = ["postgres", "react", "fastapi"]

# print(get_unique_skills(dev1, dev2))

# # ---------- Task 36 ----------

# def get_shared_permissions(role1: list[str], role2: list[str]) -> list[str]:
#     return list(set(role1) & set(role2))

# role1 = ["read", "write", "delete"]
# role2 = ["read", "execute", "write"]

# print(get_shared_permissions(role1, role2))

# # ---------- Task 37 ----------

# def get_pending_notifications(target: list[str], sent: list[str]) -> list[str]:
#     return list(set(target) - set(sent))

# target = ["user1", "user2", "user3", "user4"]
# sent = ["user2", "user4", "user5"]

# print(get_pending_notifications(target, sent))