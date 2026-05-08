import sqlite3

# 1. Establish connection to an in-memory database
conn = sqlite3.connect(':memory:')

# 2. Create a cursor object to interact with the database
cursor = conn.cursor()

# 3. Define the database schema
cursor.execute('''
CREATE TABLE apartments (
    id INTEGER PRIMARY KEY,
    label TEXT,
    price INTEGER
)
''')

# 4. Populate the table with sample data
sample_data = [
    ('Warsaw Central', 600000),
    ('Krakow North', 450000),
    ('Wroclaw West', 700000),
    ('Warsaw West', 520000)
]
cursor.executemany('INSERT INTO apartments (label, price) VALUES (?, ?)', sample_data)

# # 5. Execute SQL query using LIKE operator for pattern matching
# sql_query = "SELECT * FROM apartments WHERE label LIKE '%Warsaw%'"
# cursor.execute(sql_query)

# # 6. Fetch and display the results
# results = cursor.fetchall()

# print("Found apartments:")
# for row in results:
#     print(f"- {row[1]}: {row[2]} PLN")

cursor.execute("UPDATE apartments SET price = 650000 WHERE label ='Warsaw Central'")

cursor.execute("SELECT * FROM apartments")

results = cursor.fetchall()

print("Found apartments:")
for row in results:
    print(f"- {row[1]}: {row[2]} PLN")

# 7. Close the connection
conn.close()