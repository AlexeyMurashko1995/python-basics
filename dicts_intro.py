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


# --- PROGRAM 3: THE DATA SANITIZER ---
print('--- Task 3: The Data Sanitizer ---')
def get_user_clean_data(raw_data: dict) -> dict:
    if not raw_data:
        return {}

    clean_data = {k: v for k, v in raw_data.items() if v is not None}

    if 'name' in clean_data:
        clean_data['name'] = clean_data['name'].upper()

    clean_data.setdefault('role', 'guest')
    return clean_data


user_dict = {
    'name': 'Alex',
    'age': None,
    'city': 'Warsaw'
}

result = get_user_clean_data(user_dict)

print(result)
print('*' * 30)


# --- PROGRAM 4: THE CURRENCY CONVERTER ---
print('--- Task 4: The Currency Converter ---')

def convert_prices_to_eur(price_data: dict, rate: float) -> dict:
    if not price_data:
        return {}
    eur_price = {k: (v * rate if rate > 0 else v) for k, v in price_data.items()}
    return eur_price


pln_prices = {'id1': 1000000, 'id2': 750000}
user_rate = 0.23

eur_prices = convert_prices_to_eur(pln_prices, user_rate)

print(eur_prices)
print('*' * 30)


# --- PROGRAM 5: THE AREA RANKER ---
print('--- Task 5: The Area Ranker ---')

def get_large_apartments(data: list, min_area: float) -> list:
    if not data:
        return {}
    large_apartments = [apartments['id'] for apartments in data if apartments['area'] >= min_area]
    return large_apartments


apartments = [
    {'id': '101', 'area': 45.5, 'price': 900000},
    {'id': '102', 'area': 30.0, 'price': 550000},
    {'id': '103', 'area': 85.2, 'price': 2000000}
]

user_area = 31
result = get_large_apartments(apartments, user_area)

print(result)
print('*' * 30)