import pandas as pd
import sqlite3

members_data = {
    'name': ['Alex', 'Petr', 'Nikita', 'Elena', 'Veronika'],
    'age': [20, 29, 19, 25, 23],
    'months_active': [3, 23, 1, 12, 8],
    'status': ['Active', 'Expired', 'Active', 'Active', 'Expired']
}

members_df = pd.DataFrame(members_data)

gym_conn = sqlite3.connect('gym.db')

members_df.to_sql('clients', gym_conn, if_exists='replace', index=False)

sql_query = "SELECT * FROM clients WHERE months_active > 6 AND status = 'Active' ORDER BY age"

loyal_clients_df = pd.read_sql_query(sql_query, gym_conn)

print(loyal_clients_df)

gym_conn.close()

