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

# --- PROGRAM 6: THE DISTRICT FILTER ---
print('--- Task 6: The district filter ---')


def get_prices_by_district(data: list, target_district: str) -> list:
    if not data:
        return []
    district_list = [flat['price'] for flat in data if flat['district'] == target_district]
    return district_list


apartments = [
    {'id': 1, 'district': 'Wola', 'price': 950000},
    {'id': 2, 'district': 'Mokotów', 'price': 1200000},
    {'id': 3, 'district': 'Wola', 'price': 700000},
    {'id': 4, 'district': 'Ursus', 'price': 500000}
]

user_district = 'Wola'

result = get_prices_by_district(apartments, user_district)

print(result)
print('*' * 30)

# --- PROGRAM 7: THE BUDGET FILTER ---
print('--- Task 7: The Budget Filter ---')


def filter_by_max_price(data_list: list, max_price: int) -> list:
    if not data_list:
        return []

    filtered_apartment = [flat for flat in data_list if flat['price'] <= max_price]
    return filtered_apartment


apartments = [
    {'id': 1, 'district': 'Wola', 'price': 950000},
    {'id': 2, 'district': 'Mokotów', 'price': 1200000},
    {'id': 3, 'district': 'Ursus', 'price': 500000}
]

user_budget = 960000
result_list = filter_by_max_price(apartments, user_budget)

print(result_list)
print('*' * 30)

# --- PROGRAM 8: THE PRICE FORMATTER ---
print('--- Task 8: The Price Formatter ---')


def format_apartment_stats(data_list: list) -> list:
    if not data_list:
        return []
    formatted_list = [f'ID: {flat['id']}, District: {flat['district']}, Price: {flat['price']}' for flat in data_list]
    return formatted_list


apartments = [
    {'id': 1, 'district': 'Wola', 'price': 950000},
    {'id': 2, 'district': 'Mokotów', 'price': 1200000}
]

filtered_list = format_apartment_stats(apartments)

print(filtered_list)
print('*' * 30)

# --- PROGRAM 9: UPDATE AND ADD
print('--- Task 9: Update And Add')

prices = {'apple': 5, 'banana': 3}

prices['apple'] = 6
prices['orange'] = 4

print(f'Prices: {prices}')
print('*' * 30)

# --- PROGRAM 10: AGGREGATION ---
print('--- Task 10: Aggregation ---')

sales = [
    {'category': 'tech', 'price': 100},
    {'category': 'home', 'price': 50},
    {'category': 'tech', 'price': 200},
    {'category': 'home', 'price': 30}
]

report = {}

for sale in sales:
    sale_name = sale['category']
    sale_price = sale['price']
    if sale_name not in report:
        report[sale_name] = sale_price
    else:
        report[sale_name] += sale_price

print(report)
print('*' * 30)

# --- PROGRAM 11: NESTED LOGIC ---
print('--- Task 11: Nested Logic ---')

items = [
    {'cat': 'food', 'name': 'bread', 'p': 2},
    {'cat': 'food', 'name': 'meat', 'p': 15},
    {'cat': 'auto', 'name': 'oil', 'p': 50},
    {'cat': 'auto', 'name': 'tire', 'p': 120}
]

max_prices = {}

for item in items:
    item_name = item['cat']
    item_price = item['p']
    if item_name not in max_prices:
        max_prices[item_name] = item_price
    else:
        if max_prices[item_name] < item_price:
            max_prices[item_name] = item_price

print(max_prices)
print('*' * 30)

# --- PROGRAM 12: WAREHOUSE INVENTORY: COUNTING ---
print('--- Task 12: Warehouse Inventory: Counting ---')

cargo = ['box', 'pallet', 'box', 'box', 'container', 'pallet']

inventory = {}

for item in cargo:
    if item not in inventory:
        inventory[item] = 1
    else:
        inventory[item] += 1

print(inventory)
print('*' * 30)

# --- PROGRAM 13: NESTED AGGREGATION ---
print('--- Task 13: Nested Aggregation ---')

sales_data = [
    {'dept': 'A', 'rev': 100},
    {'dept': 'B', 'rev': 200},
    {'dept': 'A', 'rev': 300}
]

report = {}

for sale in sales_data:
    sale_dept = sale['dept']
    sale_profit = sale['rev']

    if sale_dept not in report:
        report[sale_dept] = {'total': sale_profit, 'count': 1}
    else:
        report[sale_dept]['total'] += sale_profit
        report[sale_dept]['count'] += 1

print(report)
print('*' * 30)

# --- PROGRAM 14: DATA FILTERING (CONDITIONS) ---
print('--- Task 14: Data Filtering (Conditions) ---')

cars = {'Tesla': 50000, 'BMW': 40000, 'Lada': 5000, 'Ford': 15000}

expensive_cars = {k: v for k, v in cars.items() if v > 20000}

print(expensive_cars)
print('*' * 30)

# --- PROGRAM 15: AI DATA PREPROCESSING (FULL CYCLE) ---
print('--- Task 15: AI Data Preprocessing (Full Cycle) ---')

raw_data = [
    {'dist': 'Wola', 'p': 800000},
    {'dist': 'Mokotów', 'p': 0},      # Buggy data!
    {'dist': 'Wola', 'p': 750000},
    {'dist': 'Mokotów', 'p': 950000},
    {'dist': 'Wola', 'p': 100}        # Too cheap (anomaly!)
]

clean_data = [raw for raw in raw_data if raw['p'] > 10000]
final_stats = {}

for ad in clean_data:
    ad_name = ad['dist']
    ad_price = ad['p']
    if ad_name not in final_stats:
        final_stats[ad_name] = {'total': ad_price, 'count': 1}
    else:
        final_stats[ad_name]['total'] += ad_price
        final_stats[ad_name]['count'] += 1

print(final_stats)
print('*' * 30)

# --- PROGRAM 16: REAL ESTATE MARKET ANALYTICS ---
print('--- Task 16: Real Estate Market Analytics ---')

district_stats = {
    'Wola': {'total': 1550000, 'count': 2},
    'Mokotów': {'total': 950000, 'count': 1},
    'Ursynów': {'total': 2400000, 'count': 3},
    'Praga': {'total': 800000, 'count': 2}
}

average_prices = {}

max_avg = 0
expensive_district = ''

for district, stats in district_stats.items():
    average = stats['total'] / stats['count']
    if average >= max_avg:
        max_avg = average
        expensive_district = district
    if district not in average_prices:
        average_prices[district] = average

print(max_avg)
print(expensive_district)
print(average_prices)

print('*' * 30)
