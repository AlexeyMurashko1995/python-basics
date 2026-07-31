import sqlite3

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

with open('sql_pr.sql', 'r', encoding='utf-8') as file:
    sql_script = file.read()

cursor.executescript(sql_script)

query = "SELECT city, COUNT(*) AS delivered_count, SUM(weight_kg) AS total_weight FROM orders WHERE status='delivered' GROUP BY city"
cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)

