import pandas as pd
import sqlite3

cargo_data = {
    'id_tracking': ['PL001', 'PL002', 'PL003', 'PL004', 'PL005', 'PL006', 'PL007'],
    'destination': ['Warsaw', 'Gdansk', 'Wroclaw', 'Katowice', 'Krakow', 'Lublin', 'Poznan'],
    'weight': [612, 499, 43, 501, 710, 550, 205],
    'status': ['Delivered', 'In Transit', 'Delivered', 'Delivered', 'In Transit', 'Delivered', 'In Transit']
}

df_cargo = pd.DataFrame(cargo_data)

conn = sqlite3.connect('logistics.db')

df_cargo.to_sql('cargo', conn, if_exists='replace', index=False)

sql_query = "SELECT * FROM cargo WHERE weight > 500 AND status = 'In Transit'"

filtered_cargo = pd.read_sql_query(sql_query, conn)

print(filtered_cargo)

conn.close()