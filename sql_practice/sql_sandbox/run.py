import sqlite3

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

with open('sql_pr.sql', 'r', encoding='utf-8') as file:
    sql_script = file.read()

cursor.executescript(sql_script)

# query = "SELECT city, COUNT(*) AS delivered_count, SUM(weight_kg) AS total_weight FROM orders WHERE status='delivered' GROUP BY city"
# query = "SELECT client_name, city, weight_kg FROM orders WHERE status = 'in_transit'"
# query = "SELECT city, SUM(weight_kg) AS total_weight FROM orders GROUP BY city HAVING SUM(weight_kg) > 100"
# query = "SELECT city, SUM(weight_kg) AS total_weight FROM orders WHERE status = 'delivered' GROUP BY city HAVING SUM(weight_kg) > 100"
query = "SELECT city, COUNT(*) AS total_count FROM orders WHERE weight_kg > 40 GROUP BY city HAVING COUNT(*) >= 2"

cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)

