import pandas as pd
import sqlite3

cargo_data = {
    'tracking_id': ['PL001', 'PL002', 'PL003', 'PL004', 'PL005'],
    'destination': ['Warsaw', 'Gdansk', 'Sopot', 'Krakow', 'Wroclaw'],
    'weight_kg': [2, 12, 1, 34, 45],
    'status': ['Delivered', 'In Transit', 'In Transit', 'Delivered', 'Delivered']
}

cargo_df = pd.DataFrame(cargo_data)

conn = sqlite3.connect('cargo.db')

cargo_df.to_sql('cargo', conn, if_exists='replace', index=False)

sql_query = "SELECT * FROM cargo WHERE weight_kg > 10"

heavy_packages_df = pd.read_sql_query(sql_query, conn)

print(heavy_packages_df)

conn.close()