# --- PROGRAM 1: DICTIONARY CRUD AND LOGIC ---
print('--- Task 1: Dictionary CRUD And Logic ---')

flat_info = {
    'city': 'Warsaw',
    'flat_type': 'apartment',
    'price per meter': 19000,
    'area': 49.6
}

flat_info['price per meter'] = flat_info['price per meter'] + (flat_info['price per meter'] * 0.1)
flat_info['is_expensive'] = flat_info['price per meter'] > 15000

print(flat_info)
print('*' * 30)

# --- PROGRAM 2: REAL ESTATE PRICE ANALYZER ---
print('--- Task 2: Real Estate Price Analyzer ---')


def calculate_average_price(data_list):
    if not data_list:
        return 0
    else:
        total_price = sum(apartment['price'] for apartment in data_list)
        return round(total_price / len(data_list), 2)


apartments_data = [
    {'price': 950000, 'area': 45.5, 'district': 'Wola'},
    {'price': 1200000, 'area': 60.0, 'district': 'Mokotów'},
    {'price': 700000, 'area': 30.2, 'district': 'Ursus'}
]

average_price = calculate_average_price(apartments_data)

print(f'Average price: {average_price}')
print('*' * 30)