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

# --- 3. ARCHIVED PRACTICES ---
"""
# Archived for reference:
# 1. Pattern matching: LIKE '%Warsaw%'
# 2. Update: SET price = 650000
# 3. Delete: WHERE label = 'Krakow North'
"""

# --- 4. CURRENT PRACTICE: SELECTING THE BEST OPTION ---
# Goal: Find the cheapest apartment in Warsaw
cursor.execute("""
    SELECT * FROM apartments
    WHERE label LIKE '%Warsaw%'
    ORDER BY price ASC
    LIMIT 1
""")

# fetchone() returns a single tuple (row) or None
result = cursor.fetchone()

print("--- Search Result ---")
if result:
    # Formatting the output: index 1 is label, index 2 is price
    print(f"Cheapest option in Warsaw: {result[1]} - {result[2]} PLN")
else:
    print("No apartments found matching your criteria.")

# --- 5. CLEANUP ---
conn.close()