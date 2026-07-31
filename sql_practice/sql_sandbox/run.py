import sqlite3

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

with open('sql_pr.sql', 'r', encoding='utf-8') as file:
    sql_script = file.read()

cursor.executescript(sql_script)

query = 'SELECT client_name, city, weight_kg FROM orders WHERE status= "delivered"'
cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)

