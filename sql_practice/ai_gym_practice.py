import pandas as pd
import sqlite3
from google import genai

conn = sqlite3.connect('gym.db')

sql_query = "SELECT * FROM clients"

all_clients_df = pd.read_sql_query(sql_query, conn)

conn.close()

df_text = all_clients_df.to_string()

print(df_text)