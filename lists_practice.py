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

# --- PROGRAM 28: SPAM FILTER ---
print('--- Task 28: Spam Filter ---')

count_messages = int(input('Enter the count of messages: '))
messages_list = [input('Enter the message: ') for _ in range(count_messages)]
spam_count = int(input('Enter the count of spam words: '))
spam_list = [input('Enter the spam words: ').lower() for _ in range(spam_count)]

filtered_list = []

for message in messages_list:
    is_spam = False
    for spam in spam_list:
        if spam in message.lower():
            is_spam = True
            break
    if not is_spam:
        filtered_list.append(message)

print(*filtered_list, sep='\n')
print('*' * 30)

# --- PROGRAM 29: LOG SEARCH ---
print('--- Task 29: Log Search ---')

count_logs = int(input('Enter the count of logs: '))
logs_list = [input('Enter the log: ') for _ in range(count_logs)]

filtered_list = []

for logs in logs_list:
    if 'ERROR' in logs and 'CRITICAL' in logs and 'RESOLVED' not in logs:
        filtered_list.append(logs)

print(*filtered_list, sep='\n')
print('*' * 30)

# --- PROGRAM 30: SMART TAG SEARCH ---
print('--- Task 30: Smart Tag Search ---')

description_count = int(input('Enter the count of descriptions: '))
descriptions_list = [input('Enter the description: ') for _ in range(description_count)]
tags_phrase = input('Enter the tags: ').lower().split()

filtered_list = []

for description in descriptions_list:
    count = 0
    for tags in tags_phrase:
        if tags in description.lower():
            count += 1
    if count == len(tags_phrase):
        filtered_list.append(description)

print(*filtered_list, sep='\n')
print('*' * 30)

# --- PROGRAM 31: INTERSECTION ---
print('--- Task 31: Intersection ---')

first_count = int(input('Enter the count of words: '))
first_list = [input('Enter the word: ') for _ in range(first_count)]

second_count = int(input('Enter the count of words: '))
second_list = [input('Enter the word: ') for _ in range(second_count)]

intersection_list = []

for word in first_list:
    if word in second_list:
        intersection_list.append(word)

print(*intersection_list, sep='\n')
print('*' * 30)

# --- PROGRAM 32: FUZZY SEARCH ---
print('--- Task 32: Fuzzy Search ---')

tags_search = input('Enter the tags(at least 3): ').lower().split()
threshold = 2
phrase_list = [input('Enter the phrase: ') for _ in range(3)]

final_list = []

for phrase in phrase_list:
    count = 0
    for tag in tags_search:
        if tag in phrase.lower():
            count += 1
    if count >= threshold:
        final_list.append(phrase)

print(*final_list, sep='\n')
print('*' * 30)

# --- PROGRAM 33: SPECIAL CHARACTERS HANDLED ---
print('--- Task 33: Special Characters Handled ---')

tags_count = int(input('Enter the count of tags: '))
tags_list = [input('Enter the tag: ').lower() for _ in range(tags_count)]
phrase_count = int(input('Enter the count of phrases: '))
phrase_list = [input('Enter the phrase: ') for _ in range(phrase_count)]

final_list = []

for phrase in phrase_list:
    count = 0
    for tag in tags_list:
        if tag in phrase.lower():
            count += 1
    if count == len(tags_list):
        final_list.append(phrase)

print(*final_list, sep='\n')
print('*' * 30)

# --- PROGRAM 34: FILE SCANNER ---
print('--- Task 34: File Scanner ---')

files_count = int(input('Enter the count of files: '))
files_list = [input('Enter the file name: ').lower() for _ in range(files_count)]

alerts_count = int(input('Enter the count of alerts: '))
alerts_list = [input('Enter the alert: ').lower() for _ in range(alerts_count)]

filtered_list = []

for file in files_list:
    is_alert = False
    for alert in alerts_list:
        if alert in file:
            is_alert = True
            break
    if not is_alert:
        filtered_list.append(file)

print(*filtered_list, sep='\n')
print('*' * 30)

# --- PROGRAM 35: REVIEW SENTIMENT ---
print('--- Task 35: Review Sentiment ---')

review_count = int(input('Enter the count of reviews: '))
reviews_list = [input('Enter the review: ') for _ in range(review_count)]

positive_count = int(input('Enter the count of positive words: '))
positive_words = [input('Enter the word: ').lower() for _ in range(positive_count)]

filtered_review = []

for review in reviews_list:
    count = 0
    for word in positive_words:
        if word in review.lower():
            count += 1
    if count >= 3:
        filtered_review.append(review)

print(*filtered_review, sep='\n')
print('*' * 30)

# --- PROGRAM 36: LINE-BY-LINE OUTPUT ---
print('--- Task 36: Line-By-Line Output ---')

phrase = input('Enter the phrase: ').split()

print(*phrase, sep='\n')
print('*' * 30)

# --- PROGRAM 37: INITIALS ---
print('--- Task 37: Initials ---')

phrase_list = input('Enter your initials: ').split()
initial_list = [word[0] for word in phrase_list]

print(*initial_list, sep='.', end='.')
print('*' * 30)

# --- PROGRAM 38: WINDOWS OS ---
print('--- Task 38: Windows OS')

phrase = input('Enter the phrase: ').split('\\')

print(*phrase, sep='\n')
print('*' * 30)

# --- PROGRAM 39: DIAGRAM ---
print('--- Task 39: Diagram ---')

phrase_list = '5 6 7 8 9'.split()
output_list = []

for i in range(len(phrase_list)):
    phrase_list[i] = int(phrase_list[i])

for phrase in phrase_list:
    result = phrase * '*'
    output_list.append(result)

print(*output_list, sep='\n')
print('*' * 30)

# --- PROGRAM 40: DIAGRAM 2.0 ---
print('--- Task 40: Diagram 2.0 ---')

diagram = [int(num) * '+' for num in input().split()]

print(*diagram, sep='\n')
print('*' * 30)

# --- PROGRAM 41: VALID IP ADDRESS ---
print('--- Task 41: Valid IP Address ---')

ip_list = input('Enter the address: ').split('.')

for i in range(len(ip_list)):
    ip_list[i] = int(ip_list[i])

is_valid = True

for ip in ip_list:
    if 0 <= ip <= 255:
        is_valid = True
    else:
        is_valid = False
        break

if is_valid:
    print('YES')
else:
    print('NO')

print('*' * 30)

# --- PROGRAM 42: ADD A SEPARATOR ---
print('--- Task 42: Add A Separator ---')

word = input('Enter the word: ')
separator = input('Enter the separator: ')

print(separator.join(word))
print('*' * 30)

# --- PROGRAM 43: NUMBER OF MATCHING PAIRS ---
print('--- Task 43: Number Of Matching Pairs ---')

phrase_str = input('Enter the phrase: ').split()
phrase_int = [int(phrase) for phrase in phrase_str]

count = 0

for i in range(len(phrase_int)):
    for j in range(i + 1, len(phrase_int)):
        if phrase_int[i] == phrase_int[j]:
            count += 1

print(count)
print('*' * 30)

# --- PROGRAM 44: COMBINATIONS 3.0 ---
print('--- Task 44: Combinations 3.0 ---')

phrase_str = input('Enter the phrase: ').split()
phrase_int = [int(num) for num in phrase_str]

count = 0

for i in range(len(phrase_int)):
    for j in range(i + 1, len(phrase_int)):
        for k in range(j + 1, len(phrase_int)):
            if phrase_int[i] == phrase_int[j] == phrase_int[k]:
                count += 1

print(count)
print('*' * 30)

# --- PROGRAM 45: AI PRE-PROCESSING ---
print('--- Task 45: AI Pre-Processing--- ')

phrase_str = input('Enter the phrase: ').split()
phrase_int = [int(num) for num in phrase_str]

count = 0

for i in range(len(phrase_int)):
    for j in range(i + 1, len(phrase_int)):
        if abs(phrase_int[i] - phrase_int[j]) <= 5000:
            count += 1

print(count)
print('*' * 30)

# --- PROGRAM 46: NEW LOT ---
print('--- Task 46: New Lot ---')

price_list = [580000, 620000, 750000, 900000]

price_list.insert(1, 600000)

print(price_list)
print('*' * 30)

# --- PROGRAM 47: SPECIAL CHARS ---
print('--- Task 47: Special Chars ---')

numbers_list = [10, -5, 20, -3, 30]

for i in range(len(numbers_list) - 1, -1, -1):
    if numbers_list[i] < 0:
        numbers_list.insert(i, 0)

print(numbers_list)
print('*' * 30)

# --- PROGRAM 48: VIP-QUEUE ---
print('--- Task 48: VIP-Queue ---')

tasks = ['Fix bug', 'Update docs', 'CRITICAL: Server down', 'Drink coffee', 'CRITICAL: Database error']
final_tasks = []

for task in tasks:
    if 'CRITICAL' in task:
        final_tasks.insert(0, task)
    else:
        final_tasks.append(task)

print(final_tasks)
print('*' * 30)

# --- PROGRAM 49: ID-NUMBER ---
print('--- Task 49: ID-Number ---')

ids = [1024, 2048, 3072, 4096, 5120]

if 4096 in ids:
    print(f'Object found at index: {ids.index(4096)}')
else:
    print('Object not found')

print('*' * 30)

# --- PROGRAM 50: SECOND CRITICAL FAILURE ---
print('--- Task 50: Second Critical Failure ---')

tasks = ['Fix bug', 'CRITICAL: Error 1', 'Update docs', 'CRITICAL: Error 2', 'Drink coffee']

first_pos = tasks.index('CRITICAL: Error 1')
second_pos = tasks.index('CRITICAL: Error 2')

print(first_pos, second_pos)
print('*' * 30)

# --- PROGRAM 51: SOLD LOT ---
print('--- Task 51: Sold Lot ---')

prices = [450000, 520000, 610000, 520000, 700000]

prices.remove(520000)

print(prices)
print('*' * 30)

# --- PROGRAM 52: SECURE DISPOSAL ---
print('--- Task 52: Secure Disposal ---')

stock = ['Apples', 'Oranges', 'DAMAGED', 'Bananas']

if 'DAMAGED' in stock:
    stock.remove('DAMAGED')
else:
    print('Object not found')

print(*stock)
print('*' * 30)