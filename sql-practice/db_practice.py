import sqlite3

# --- 1. DATABASE SETUP ---
# Establishing connection to an in-memory database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Defining the database schema
cursor.execute('''
CREATE TABLE apartments (
    id INTEGER PRIMARY KEY,
    label TEXT,
    price INTEGER
)
''')

# --- 2. DATA POPULATION ---
sample_data = [
    ('Warsaw Central', 600000),
    ('Krakow North', 450000),
    ('Wroclaw West', 700000),
    ('Warsaw West', 520000)
]
cursor.executemany('INSERT INTO apartments (label, price) VALUES (?, ?)', sample_data)

# --- 3. ARCHIVED PRACTICES (Commented for reference) ---
"""
# Pattern matching (LIKE)
sql_query = "SELECT * FROM apartments WHERE label LIKE '%Warsaw%'"
cursor.execute(sql_query)
results = cursor.fetchall()

# Update operation
cursor.execute("UPDATE apartments SET price = 650000 WHERE label ='Warsaw Central'")

# Delete operation
cursor.execute("DELETE FROM apartments WHERE label = 'Krakow North'")
"""

# --- 4. CURRENT PRACTICE: SORTING ---
# Selecting all apartments sorted by price in ascending order
cursor.execute("SELECT * FROM apartments ORDER BY price ASC")
results = cursor.fetchall()

print("List of apartments (Sorted by Price):")
for row in results:
    print(f"- {row[1]}: {row[2]} PLN")

# --- 5. CLEANUP ---
conn.close()