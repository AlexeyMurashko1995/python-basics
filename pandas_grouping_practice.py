import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


pd.options.display.float_format = '{:.2f}'.format

# Load the dataset
df = pd.read_csv('warsaw_apartments.csv', encoding='utf-8-sig')

# Data cleaning: calculate and drop temporary column, rename districts
df['price_usd'] = df['price'] * 0.25
df = df.drop('price_usd', axis=1)

df = df.rename(columns={
    'district': 'area_name',
    'price per meter 2': 'price_m2'
})

#Finding missing values
empty_fields = df.isna().sum()
df['rooms'] = df['rooms'].fillna(df['rooms'].median())

#Filter price outliers
df = df[(df['price_m2'] > 8000) & (df['price_m2'] < 50000)]

#Save clean data
df.to_csv('apartments_clean.csv', index=False, encoding='utf-8-sig')

#Correlation calculation
correlation_matrix = df.corr(numeric_only=True)
df.plot(kind='scatter', x='area', y='price', alpha=0.5)

#Creating boxplot
df.boxplot(column='price_m2', by='area_name', figsize=(12, 6))

plt.xticks(rotation=45)
plt.show()

#Starting work with scikit-learn
df_with_districts = pd.get_dummies(df, columns=['area_name'], drop_first=True)

X = df_with_districts.drop(['price', 'price_m2'], axis=1)
y = df_with_districts['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)

print(f'Model accuracy (R2 score): {score}')

y_pred = model.predict(X_test)

comparison = pd.DataFrame({
    'Actual': y_test.values[:5],
    'Predicted': y_pred[:5]
})

print(comparison)

new_apartment = pd.DataFrame(0, index=[0], columns=X.columns)

new_apartment['area'] = 52.0
new_apartment['rooms'] = 2

if 'area_name_Mokotów' in new_apartment.columns:
    new_apartment['area_name_Mokotów'] = 1

predicted_price = model.predict(new_apartment)
print(f'Predicted price: {predicted_price[0]:,.2f} zł')


# grouped = df.groupby('area_name')

# agg_info = grouped['price'].agg(['min', 'max', 'count'])
# agg_info = agg_info[agg_info['count'] > 10]

# filtered_agg_info = agg_info.sort_values('min').plot(kind='bar')

#plt.show()

