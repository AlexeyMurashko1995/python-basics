import sqlite3

# 1. Setup database connection
conn = sqlite3.connect("warehouse.db")
cursor = conn.cursor()

# 2. Create table if it doesn't exist (using correct INTEGER type)
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    quantity INTEGER,
    price REAL
)
''')

# 3. Prepare initial data
products_data = [
    ('Laptop', 'Electronics', 5, 1200.50),
    ('Smartphone', 'Electronics', 0, 800.00),
    ('Keyboard', 'Peripherals', 15, 45.99),
    ('Monitor', 'Electronics', 10, 300.00),
    ('Mouse', 'Peripherals', 20, 25.50)
]

# Clean table and insert new data to avoid duplicates on rerun
cursor.execute("DELETE FROM products")
cursor.executemany("INSERT INTO products (name, category, quantity, price) VALUES (?, ?, ?, ?)", products_data)

# # 4. Business logic: Update price and Delete out-of-stock items
# cursor.execute("UPDATE products SET price = 1250.50 WHERE name = 'Laptop'")
# cursor.execute("DELETE FROM products WHERE quantity = 0")

# # 5. Save changes to the database file
# conn.commit()

# # 6. Generate a formatted warehouse report
# print("--- CURRENT INVENTORY REPORT ---")
# cursor.execute("SELECT name, category, quantity, price FROM products ORDER BY price DESC")
# products = cursor.fetchall()

# for item in products:
#     name, cat, qty, price = item
#     # Using alignment formatting for a clean table-like output
#     print(f"Product: {name:<12} | Category: {cat:<12} | Qty: {qty:<3} | Price: {price:>8.2f}")

# # 7. Finding total inventory value
# cursor.execute("SELECT SUM(price*quantity) FROM products")

# total_value = cursor.fetchone()[0]

# print(f'Total inventory value:\n{total_value} USD')

# # 8. Product Statistics
# cursor.execute("SELECT AVG(price) FROM products")
# result = cursor.fetchone()[0]

# print(f'Average price: {result:.2f} USD')

# cursor.execute("SELECT * FROM products ORDER BY price DESC LIMIT 1")
# max_price_item = cursor.fetchall()

# for item in max_price_item:
#     print(f'The most expensive item:\n{item[1]}, price: {item[4]} USD')

# 9. Advanced Filtering
cursor.execute("SELECT * FROM products WHERE name LIKE '%o%'")
result = cursor.fetchall()

for item in result:
    print(f'Product name with "o": {item[1]}')

cursor.execute("SELECT * FROM products WHERE price BETWEEN 50 and 1000")
result = cursor.fetchall()

for item in result:
    print(f'Product names with price between 50 and 1000 USD: {item[1]}, price: {item[4]} USD')

# 10. Close the database connection
conn.close()