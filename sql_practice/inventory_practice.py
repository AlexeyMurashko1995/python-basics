import sqlite3

conn = sqlite3.connect("warehouse.db")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY, name TEXT, category TEXT, quantity INTEGER, price REAL)
''')

products_data = [
    ('Laptop', 'Electronics', 5, 1200.50),
    ('Smartphone', 'Electronics', 0, 800.00),
    ('Keyboard', 'Peripherals', 15, 45.99),
    ('Monitor', 'Electronics', 10, 300.00),
    ('Mouse', 'Peripherals', 20, 25.50)
]

cursor.executemany("INSERT INTO products (name, category, quantity, price) VALUES (?, ?, ?, ?)", products_data)

cursor.execute("SELECT * FROM products")

result = cursor.fetchall()

print(result)

conn.commit()