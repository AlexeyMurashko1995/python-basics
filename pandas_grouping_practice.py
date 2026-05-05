import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('apartments_lab.csv', encoding='utf-8-sig')

# Data cleaning: calculate and drop temporary column, rename districts
df['price_usd'] = df['price'] * 0.25
df = df.drop('price_usd', axis=1)

df = df.rename(columns={
    'district': 'area_name',
    'price per meter 2': 'price_m2'
})

#Finding missing values
empty_fields = df.isna().sum()

print(empty_fields)

# grouped = df.groupby('area_name')

# agg_info = grouped['price'].agg(['min', 'max', 'count'])
# agg_info = agg_info[agg_info['count'] > 10]

# filtered_agg_info = agg_info.sort_values('min').plot(kind='bar')

# plt.show()

