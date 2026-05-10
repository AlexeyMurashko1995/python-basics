import sqlite3

# 1. Constants
DB_NAME = "warehouse.db"

def manage_inventory():
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # 2. Table creation
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            quantity INTEGER,
            price REAL
        )
        ''')

        # 3. Initial data preparation
        products_data = [
            ('Laptop', 'Electronics', 5, 1200.50),
            ('Smartphone', 'Electronics', 0, 800.00),
            ('Keyboard', 'Peripherals', 15, 45.99),
            ('Monitor', 'Electronics', 10, 300.00),
            ('Mouse', 'Peripherals', 20, 25.50)
        ]

        cursor.execute("DELETE FROM products")
        cursor.executemany("INSERT INTO products (name, category, quantity, price) VALUES (?, ?, ?, ?)", products_data)

        # 4. Business logic: Update and Delete
        cursor.execute("UPDATE products SET price = 1250.50 WHERE name = 'Laptop'")
        cursor.execute("DELETE FROM products WHERE quantity = 0")

        # 5. Saving changes
        conn.commit()

        # 6. Inventory report
        print("--- CURRENT INVENTORY REPORT ---")
        cursor.execute("SELECT name, category, quantity, price FROM products ORDER BY price DESC")
        products = cursor.fetchall()

        for item in products:
            name, cat, qty, price = item
            print(f"Product: {name:<12} | Category: {cat:<12} | Qty: {qty:<3} | Price: {price:>8.2f}")

        # 7. Total inventory value
        cursor.execute("SELECT SUM(price*quantity) FROM products")
        total_value = cursor.fetchone()[0]
        print(f'\nTotal inventory value: {total_value:.2f} USD')

        # 8. Product statistics
        cursor.execute("SELECT AVG(price) FROM products")
        avg_price = cursor.fetchone()[0]
        print(f'Average price: {avg_price:.2f} USD')

        cursor.execute("SELECT * FROM products ORDER BY price DESC LIMIT 1")
        max_price_item = cursor.fetchone()
        if max_price_item:
            print(f'The most expensive item: {max_price_item[1]}, price: {max_price_item[4]:.2f} USD')

        # 9. Advanced filtering
        print("\n--- FILTERED RESULTS ---")
        cursor.execute("SELECT * FROM products WHERE name LIKE '%o%'")
        result_o = cursor.fetchall()
        for item in result_o:
            print(f'Product with "o": {item[1]}')

        cursor.execute("SELECT * FROM products WHERE price BETWEEN 50 AND 1000")
        result_range = cursor.fetchall()
        for item in result_range:
            print(f'Product between 50-1000 USD: {item[1]}, price: {item[4]:.2f} USD')

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    manage_inventory()