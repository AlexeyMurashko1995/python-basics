import sqlite3

# 1. Constants
DB_NAME = "warehouse.db"

def create_table(cursor):
    """Creates the products table if it doesn't exist."""
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        quantity INTEGER,
        price REAL
    )
    ''')

def get_initial_products(cursor):
    """Prepares and inserts the initial set of products."""
    products_data = [
        ('Laptop', 'Electronics', 5, 1200.50),
        ('Smartphone', 'Electronics', 0, 800.00),
        ('Keyboard', 'Peripherals', 15, 45.99),
        ('Monitor', 'Electronics', 10, 300.00),
        ('Mouse', 'Peripherals', 20, 25.50)
    ]

    cursor.execute("DELETE FROM products")
    cursor.executemany("INSERT INTO products (name, category, quantity, price) VALUES (?, ?, ?, ?)", products_data)

def update_laptop_price(cursor):
    """Handles user input to update the price of the Laptop."""
    try:
        user_price = input('Enter new price for Laptop: ')
        new_price = float(user_price)
        cursor.execute("UPDATE products SET price = ? WHERE name = 'Laptop'", (new_price,))
        print(f'You successfully updated the price for Laptop to {new_price}')
    except ValueError:
        print('You must enter numbers, not text!')

def show_inventory_report(cursor):
    """Displays a formatted report of all products in the database."""
    print("\n--- CURRENT INVENTORY REPORT ---")
    cursor.execute("SELECT name, category, quantity, price FROM products ORDER BY price DESC")
    products = cursor.fetchall()

    for item in products:
        name, cat, qty, price = item
        print(f"Product: {name:<12} | Category: {cat:<12} | Qty: {qty:<3} | Price: {price:>8.2f}")

def show_statistics(cursor):
    """Calculates and prints general inventory statistics."""
    cursor.execute("SELECT SUM(price*quantity) FROM products")
    total_value = cursor.fetchone()[0]
    print(f'\nTotal inventory value: {total_value:.2f} USD')

    cursor.execute("SELECT AVG(price) FROM products")
    avg_price = cursor.fetchone()[0]
    print(f'Average price: {avg_price:.2f} USD')

    cursor.execute("SELECT * FROM products ORDER BY price DESC LIMIT 1")
    max_price_item = cursor.fetchone()
    if max_price_item:
        print(f'The most expensive item: {max_price_item[1]}, price: {max_price_item[4]:.2f} USD')

def run_advanced_filters(cursor):
    """Applies filters to show specific subsets of products."""
    print("\n--- FILTERED RESULTS ---")
    cursor.execute("SELECT * FROM products WHERE name LIKE '%o%'")
    result_o = cursor.fetchall()
    for item in result_o:
        print(f'Product with "o": {item[1]}')

    cursor.execute("SELECT * FROM products WHERE price BETWEEN 50 AND 1000")
    result_range = cursor.fetchall()
    for item in result_range:
        print(f'Product between 50-1000 USD: {item[1]}, price: {item[4]:.2f} USD')

def manage_inventory():
    """Main function to orchestrate the database operations."""
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Executing the workflow
        create_table(cursor)
        get_initial_products(cursor)
        update_laptop_price(cursor)
        show_inventory_report(cursor)
        show_statistics(cursor)
        run_advanced_filters(cursor)

        conn.commit()

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