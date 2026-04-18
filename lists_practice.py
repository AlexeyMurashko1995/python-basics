# --- PROGRAM 1: APARTMENT INDEXING ---
print('--- Task 1: Apartment Indexing ---')

apartment_1 = ["Mokotow", 45, 600000]
apartment_2 = ["Wola", 38, 520000]
apartment_3 = ["Praga", 50, 480000]

apartments = [
    apartment_1,
    apartment_2,
    apartment_3
]

print(apartments[1][2])
print('*' * 30)

# --- PROGRAM 2: PRICE FILTER ---
print('--- Task 2: Price Filter ---')

prices = [550000, 720000, 480000, 950000, 610000]
expensive_apartments = []

for price in prices:
    if price > 600000:
        expensive_apartments.append(price)

print(expensive_apartments)
print('*' * 30)

# --- PROGRAM 3: DISTRICT RENT FORMATTER ---
print('--- Task 3: District Rent Formatter ---')

rent_data = [["Wola", 3500], ["Bialoleka", 2800], ["Praga", 3200]]

for district, price in rent_data:
    print(f'The rent in {district} is {price} PLN')

print('*' * 30)

# --- PROGRAM 4: NESTED LIST ITERATION ---
print('--- Task 4: Nested List Iteration ---')

data = [["Mokotow", 45], ["Wola", 38], ["Bemowo", 50]]

for district, total_area in data:
    if total_area > 40:
        print(f'Large apartment in {district}')
    else:
        print(f'Total area: {total_area}')

print('*' * 30)

# --- PROGRAM 5: CURRENCY CONVERTER ---
print('--- Task 5: Currency Converter ---')

flats_number = int(input('Enter the amount of flats: '))
pln_list = [int(input('Enter the price in PLN: ')) for _ in range(flats_number)]
eur_list = [pln_price * 0.23 for pln_price in pln_list]

print(pln_list)
print(eur_list)
print('*' * 30)

# --- PROGRAM 6: DISTRICT VALIDATOR ---
print('--- Task 6: District Validator ---')

districts = ['Wola', 'Mokotów', 'Trash', 'Praga', 'Unknown']

if 'Mokotów' in districts:
        print('Ready for analysis')

del districts[0]
del districts[-1]

print(districts)
print('*' * 30)

# --- PROGRAM 7: PRICE GAP ANALYZER ---
print('--- Task 7: Price Gap Analyzer ---')

prices = [500000, 520000, 490000, 600000]
gaps = []

for i in range(len(prices) - 1):
    diff = abs(prices[i] - prices[i + 1])
    gaps.append(diff)

print(f'Price gaps: {gaps}')
print('*' * 30)

# --- PROGRAM 8: DATA CLEANER INDICES ---
print('--- Task 8: Data Cleaner Indices ---')

raw_data = ['Wola', '', 'Mokotów', '', 'Bemowo', '', 'Praga', '']

del raw_data[1::2]

print(raw_data)
print('*' * 30)

# --- PROGRAM 9: PRICE PER METER ANALYZER ---
print('--- Task 9: Price Per Meter Analyzer ---')

flats = [["Mokotów", 600000, 40], ["Wola", 550000, 35], ["Praga", 480000, 50]]

for district, price, total_area in flats:
    square_meter = round(price / total_area, 2)
    if square_meter < 10000:
        print(f'District: {district}, Price per m2: {square_meter} - GOOD DEAL!')
    else:
        print(f'District: {district}, Price per m2: {square_meter}')

print('*' * 30)

# --- PROGRAM 10: LOGGING DISTRICTS ---
print('--- Task 10: Logging Districts ---')

districts = ['Wola', 'Mokotów', 'Ursynów', 'Bemowo']

for district in districts:
    print(f'{district} - check passed!')

print('*' * 30)

# --- PROGRAM 11: TOP 3 OFFERS ---
print('--- Task 11: Top 3 Offers ---')

prices = [3200, 3550, 4100, 4800, 5200]

for i, price in enumerate(prices[:3]):
    print(f'Lot #{i + 1}: {price} PLN')

print('*' * 30)

# --- PROGRAM 12: APARTMENT TAGS ---
print('--- Task 12: Apartment Tags ---')

tags = ['Metro', 'Parking', 'Elevator', 'Furnished', 'Renovated']

print(*tags, sep=' | ')
print('*' * 30)

# --- PROGRAM 13: SYSTEM STATUS ---
print('--- Task 13: System Status ---')

status = 'SCANNING'

print(*status, sep='...')
print(*status, sep='\n')
print('*' * 30)

# --- PROGRAM 14: DATA CLEANING ---
print('--- Task 14: Data Cleaning ---')

prices = [100, 3200, 3500, 4100, 25000, 3800]
filtered_prices = []

for price in prices:
    if 3000 <= price <= 5000:
        filtered_prices.append(str(price))

print(' --> '.join(filtered_prices))
print('*' * 30)

# --- PROGRAM 15: PARALLEL LISTS ---
print('--- Task 15: Parallel Lists ---')

districts = ['Wola', 'Mokotow', 'Bemowo']
scores = [0.85, 0.92, 0.78]

for i in range(len(districts)):
    print(f'District: {districts[i]} | Safety score: {scores[i]}', end=' ')
    print(*'SAFE', sep='-')

print('*' * 30)

# --- PROGRAM 16: CLEAN SYSTEM LOGS ---
print('--- Task 16: Clean System Logs ---')

logs = ['START', 'PROCESS_1', 'PROCESS_2', 'PROCESS_3', 'END']

print(*logs[1:-1], sep='\n\t')
print('*' * 30)

# --- PROGRAM 17: AI IMAGE NORMALIZATION ---
print('--- Task 17: AI Image Normalization ---')

raw_pixels = [0, 128, 255, 64, 200]

normalized = [raw / 255 for raw in raw_pixels]

print(*normalized, sep=' | ')
print('*' * 30)

# --- PROGRAM 18: SENSOR GRID ANALYSIS(NESTED LISTS) ---
print('--- Task 18: Sensor Grid Analysis(Nested Lists) ---')

grid = [
    [22.5, 23.0, 22.8],
    [25.4, 28.1, 26.3],
    [21.9, 22.1, 22.4]
]

for row in grid:
    for temp in row:
        if temp > 25.0:
            print(f'ALERT: {temp}°C')
        else:
            print(f'Normal: {temp}°C')
    print('---')

print('*' * 30)

# --- PROGRAM 19: AI DATA CLEANING (ANOMALY DETECTION) ---
print('--- Task 19: AI Data Cleaning (Anomaly Detection) ---')

data_stream = [14.2, 13.5, 101.1, 12.8, 98.2, 15.0, 14.7, 115.3]
anomalies = [data for data in data_stream if data > 50.0]

print(f'Detected {len(anomalies)} anomalies: {anomalies}')
print('*' * 30)

# --- PROGRAM 20: MIN-MAX SCALING (AI PREPROCESSING) ---
print('--- Task 20: Min-Max Scaling (AI Preprocessing) ---')

prices = [1200, 4500, 2300, 8900, 3100]

min_value = min(prices)
max_value = max(prices)

scaled_prices = [round((price - min_value) / (max_value - min_value), 2) for price in prices]

print(f'Min: {min_value} | Max: {max_value}')
print(f'Scaled prices: {scaled_prices}')
print('*' * 30)

# --- PROGRAM 21: WARSAW HOUSING DATA CLEANING ---
print('--- Task 21: Warsaw Housing Data Cleaning ---')


def clean_areas(areas_list: list) -> list:
    result_list = [area for area in areas_list if 10.0 < area < 500.0]
    return result_list


raw_data = [45.5, -12.0, 1000.0, 32.0, 8.5, 120.0]
result = sorted(clean_areas(raw_data))

print(f'Cleaned and sorted areas: {result}')
print('*' * 30)

# --- PROGRAM 22: NEGATIVES, POSITIVES, ZEROS
print('--- Task 22: Negatives, Positives, Zeros')

count_number = int(input('Enter the count of numbers: '))

positives_list = []
zeros_list = []
negatives_list = []

for _ in range(count_number):
    number = int(input('Enter the number: '))
    if number < 0:
        negatives_list.append(number)
    elif number > 0:
        positives_list.append(number)
    else:
        zeros_list.append(number)

full_result = negatives_list + zeros_list + positives_list
print(*full_result, sep='\n')

print('*' * 30)

# --- PROGRAM 23: NO DUBLICATES ---
print('--- Task 23: No Dublicates ---')

count_numbers = int(input('Enter the count of strings: '))
string_list = []

for _ in range(count_numbers):
    string = input('Enter the string: ')
    if string not in string_list:
        string_list.append(string)

print(*string_list, sep='\n')
print('*' * 30)

# --- PROGRAM 24: FUNCTION VALUE ---
print('--- Task 24: Function Value ---')

count_numbers = int(input('Enter the count of numbers: '))
number_list = []
function_list = []

for _ in range(count_numbers):
    number = int(input('Enter the number: '))
    number_list.append(number)
    final_number = (number ** 2) + (2 * number) + 1
    function_list.append(final_number)

print(*number_list, sep='\n')
print()
print(*function_list, sep='\n')
print('*' * 30)

# --- PROGRAM 25: REMOVE OUTLIERS ---
print('--- Task 25: Remove Outliers ---')

count_numbers = int(input('Enter the count of numbers: '))
number_list = [int(input('Enter the number: ')) for _ in range(count_numbers)]

max_value = max(number_list)
min_value = min(number_list)

filtered_list = [numbers for numbers in number_list if numbers != max_value and numbers != min_value]

print(*filtered_list, sep='\n')
print('*' * 30)

# --- PROGRAM 26: GOOGLE SEARCH - 1 ---
print('--- Task 26: Google Search - 1 ---')

string_count = int(input('Enter the count of strings: '))

string_list = [input('Enter the string: ') for _ in range(string_count)]
search_word = input('Enter the search: ').lower()

final_list = []

for string in string_list:
    if search_word in string.lower():
        final_list.append(string)

print(*final_list, sep='\n')
print('*' * 30)

# --- PROGRAM 27: GOOGLE SEARCH - 2 ---
print('--- Task 27: Google Search - 2 ---')

string_count = int(input('Enter the count of strings: '))
string_list = [input('Enter the string: ') for _ in range(string_count)]
search_word_count = int(input('Enter the count of words for search: '))
search_list = [input('Enter the word: ').lower() for _ in range(search_word_count)]

final_list = []

for phrase in string_list:
    count = 0
    for word in search_list:
        if word in phrase.lower():
            count += 1
    if count == len(search_list):
        final_list.append(phrase)

print(*final_list, sep='\n')
print('*' * 30)