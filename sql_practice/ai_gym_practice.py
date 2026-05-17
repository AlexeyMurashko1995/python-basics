import pandas as pd
import sqlite3
from google import genai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

conn = sqlite3.connect('gym.db')

sql_query = "SELECT * FROM clients"

all_clients_df = pd.read_sql_query(sql_query, conn)

conn.close()

df_text = all_clients_df.to_string()

print(df_text)

prompt = f"""Business-analytic: {df_text}"""

client = genai.Client()

response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)

conn = sqlite3.connect('gym.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS reports (report_date TEXT, report_text TEXT)""")

cursor.execute("INSERT INTO reports (report_date, report_text) VALUES (?, ?)", ('2026-05-17', response.text))

conn.commit()
conn.close()