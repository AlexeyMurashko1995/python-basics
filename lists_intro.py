# --- PROGRAM 1: THE WARSAW SHOPPING LIST ---
print('--- Task 1: The Warsaw Shopping List ---')

shopping_list = ['bread', 'meat', 'milk', 'fish', 'ice-cream']

print(f'The third element: {shopping_list[2]}')
print(f'All items: {shopping_list}')
print('*' * 30)

# --- PROGRAM 2: RANGE MAGIC ---
print('--- Task 2: Range Magic ---')

my_numbers = list(range(1, 22, 2))

print(f'The length of the list: {len(my_numbers)}')
print(f'The last: {my_numbers[10]}')
print('*' * 30)

# --- PROGRAM 3: STRING EXPLOSION ---
print('--- Task 3: String Explosion ---')

s = 'Python2026'
my_list = list(s)

print(f'My list by char: {my_list}\nIndex #6 element: {my_list[6]}')
print('*' * 30)

# --- PROGRAM 4: LIST OF NUMBERS ---
print('--- Task 4: LIST OF NUMBERS ---')

n = int(input('Enter the number: '))
my_list = list(range(1, n+1))

print(f'List of numbers: {my_list}')
print('*' * 30)

# --- PROGRAM 5: LIST 0F LETTERS ---
print('--- Task 5: List Of Letters ---')

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

n = int(input('Enter the number: '))
if n < 1 or n > 26:
    print('Invalid Input')
else:
    print(f'The letter: {abc[:n]}')
print('*' * 30)

# --- PROGRAM 6: LIST OF ODD NUMBERS ---
print('--- Task 6: List Of Odd Numbers ---')

n = int(input('Enter the number: '))

list_odd_numbers = list(range(1, n + 1, 2))

print(f'List of odd numbers from 1 to {n}: {list_odd_numbers}')
print('*' * 30)

# --- PROGRAM 7: EVERY SECOND ITEM ---
print('--- Task 7: Every Second Item ---')

luggage = '💻📘👖💳💶📷🍎👟⌚🎨'

my_luggage = list(luggage)

print(f'My luggage: {my_luggage[::2]}')

print('*' * 30)

# --- PROGRAM 8: Reverse Step Slice ---
print('--- Task 8: Reverse Step Slice ---')

phrase = 'PythonDevelopment'

filtered_phrase = list(phrase)

print(f'Filtered phrase: {filtered_phrase[::-2]}')
print('*' * 30)

# --- PROGRAM 9: DECREMENTING RANGE ---
print('--- Task 9: Decrementing Range ---')

n = int(input('Enter the number: '))

my_list = list(range(n, -1, -5))

print(f'Decrementing range:{my_list}')
print('*' * 30)

# --- PROGRAM 10: INDEX FILTERING ---
print('--- Task 10: Index Filtering ---')

phrase = input('Enter the phrase: ')

filtered_phrase = list(phrase)

print(f'Result: {filtered_phrase[::3]}')
print('*' * 30)

# --- PROGRAM 11: THE PALINDROME LIST ---
print('--- Task 11: The Palindrome List ---')

text = input('Enter the text: ')

palindrome_list = list(text)

print(f'The palindrome list: {palindrome_list[::-1]}')
print('*' * 30)

# --- PROGRAM 12: THE MIDDLE CUT ---
print('--- Task 12: The Middle Cut ---')

text = input('Enter the text: ')

filtered_text = list(text)

print(f'Filtered text: {filtered_text[1:-1]}')
print('*' * 30)

# --- PROGRAM 13: SWAP ENDS ---
print('--- Task 13: Swap Ends ---')

phrase = input('Enter the phrase: ')

changed_phrase = list(phrase)

changed_phrase[0], changed_phrase[-1] = changed_phrase[-1], changed_phrase[0]

print(f'Changed phrase: {changed_phrase}')
print('*' * 30)

# --- PROGRAM 14: THE HIDDEN MESSAGE ---
print('--- Task 14: The Hidden Message ---')

phrase = input('Enter the phrase: ')

filtered_phrase = list(phrase[::3][::-1])

print(f'Result: {filtered_phrase}')
print('*' * 30)

# --- PROGRAM 15: THE DYNAMIC CENTER ---
print('--- Task 15: The Dynamic Center ---')

phrase = input('Enter the text: ')

filtered_phrase = list(phrase)
mid = len(filtered_phrase) // 2

print(f'Result: {filtered_phrase[mid - 1: mid + 2:]}')
print('*' * 30)

# --- PROGRAM 16: THE AI DATA SPLIT ---
print('--- Task 16: The AI Data Split ---')

full_data = list(range(1, 21))
index = int(len(full_data) * 0.8)

train_data = full_data[:index]
test_data = full_data[index:]

print(f'Train data: {train_data}\nTest data: {test_data}')
print('*' * 30)

# --- PROGRAM 17: THE STEP PROTECTOR ---
print('--- Task 17: The Step Protector ---')

phrase = input('Enter the phrase: ')

filtered_phrase = list(phrase)

print(f'Result: {filtered_phrase[-1::-4]}')
print('*' * 30)

# --- PROGRAM 18: THE SMART SWAP ---
print('--- Program 18: The Smart Swap ---')

data_list = [10, 20, 30, 40, 50, 60]

data_list[:2], data_list[4:] = data_list[4:], data_list[:2]

print(f'Result: {data_list}')
print('*' * 30)

# --- PROGRAM 19: SKIP BORDERS ---
print('--- Task 19: Skip Borders ---')


def get_core(data: list) -> list:
    return data[1:-2]


number_list = list(range(10, 70, 10))

result = get_core(number_list)

print(f'Result: {result}')
print('*' * 30)

# --- PROGRAM 20: EVERY SECOND ---
print('--- Task 20: Every Second ---')


def get_every_second_from_middle(data: list) -> list:
    return data[1:-1][::2]


my_list = list(range(0, 9))
result = get_every_second_from_middle(my_list)

print(f'Result: {result}')
print('*' * 30)

# --- PROGRAM 21: REVERSED SEGMENT ---
print('--- Task 21: Reversed Segment ---')


def get_reversed_segment(data: list, start, stop) -> list:
    return data[start:stop:][::-1]


my_list = list(range(7))
first_index = 1
last_index = 5
result = get_reversed_segment(my_list, first_index, last_index)

print(f'Result: {result}')
print('*' * 30)

# --- PROGRAM 22: CENTER CROP ---
print('--- Task 22: Center Crop ---')


def get_center_window(data: list) -> list:
    mid = len(data) // 2
    return data[mid - 1: mid + 2]


my_list = list(range(7))
result = get_center_window(my_list)

print(f'Result: {result}')
print('*' * 30)

# --- PROGRAM 23: SWAP HALVES ---
print('--- Task 23: Swap Halves ---')


def swap_halves(data: list) -> list:
    mid = (len(data) + 1) // 2
    first_half = data[:mid]
    second_half = data[mid:]
    swapped_data = second_half + first_half
    return swapped_data


my_list = list(range(1,6))
result = swap_halves(my_list)

print(f'Result: {result}')
print('*' * 30)

# --- PROGRAM 24: DATA RANGE ANALYZER ---
print('--- Task 24: Data Range Analyzer ---')


def get_workday_temperature_range(temps: list) -> int:
    #Calculates the range for the first 5 days.
    return max(temps[:5]) - min(temps[:5])


user_temps = [10, 23, 29, 21, 15, 24, 26]
diff = get_workday_temperature_range(user_temps)

print(f'Difference: {diff}')
print('*' * 30)

# --- PROGRAM 25: DATABASE SANITIZER ---
print('--- Task 25: Database Sanitizer ---')


def sanitize_user_list(users: list) -> list:
    #Checks for a bot in the list and replaces it with a security officer.
    if 'bot_12' in users:
        idx = users.index('bot_12')
        users[idx] = 'security_officer'
    return users


current_users = ['admin', 'manager', 'guest', 'bot_12', 'ceo']
clean_users = sanitize_user_list(current_users)

print(f'Clean users: {clean_users}')
print('*' * 30)

# --- PROGRAM 26: NEURAL WEIGHTS INITIALIZER ---
print('--- Task 26: Neural Weights Initializer ---')


def initialize_weights(zeros_count: int, ones_count: int) -> list:
    return [0] * zeros_count + [1] * ones_count


zeros = 10
ones = 5
weights = initialize_weights(zeros, ones)

print(f'Weights: {weights}')
print(f'Total length: {len(weights)}')
print('*' * 30)

# --- PROGRAM 27: METADATA EXTRACTOR ---
print('--- Task 27: Metadata Extractor ---')


def extract_task_metadata(tasks: list) -> str:
    """Extracts the second letter of the last task and updates it."""
    second_letter = tasks[-1][1]
    tasks[-1] = 'refactoring'
    return second_letter


my_tasks = ['mail', 'meeting', 'report', 'code_review']
letter = extract_task_metadata(my_tasks)

print(f'Second letter of last task: {letter}')
print(f'Updated tasks: {my_tasks}')
print('*' * 30)

# --- PROGRAM 28: THE MOVING AVERAGE ---
print('--- Task 28: The Moving Average ---')


def get_moving_average(sensor_data: list) -> float:
    return sum(sensor_data[-3:]) / len(sensor_data[-3:])


data_list = list(range(0, 70, 10))
result = get_moving_average(data_list)

print(f'Result: {result}')
print('*' * 30)

# --- PROGRAM 29: THE TENSOR PADDER ---
print('--- Task 29: The Tensor Padder ---')


def pad_tensor(data: list, target_size: int) -> list:
    return data + [0] * (target_size - len(data))


target = 6
original_data = [1.2, 3.4, 0.5]
result = pad_tensor(original_data, target)

print(f'Result: {result}')
print('*' * 30)

# --- PROGRAM 30: FEATURE AGGREGATOR ---
print('--- Task 30: Feature Aggregator ---')

user_interests = ['python', 'ai']
new_hobby = 'gym'
tags = ['health', 'focus']

user_interests.append(new_hobby)
user_interests.extend(tags)

print(f'User interests: {user_interests}')
print('*' * 30)

# --- PROGRAM 31: DATA STREAM CLEANER ---
print('--- Task 31: Data Stream Cleaner ---')

data = [25.5, 26.0, 999.0, 999.0, 27.2, 28.1, 999.0]

del data[2:4]
del data[-1]

print(f'Cleared data: {data}')
print('*' * 30)

# --- PROGRAM 32: THE "NONE" TRAP ---
print('--- Task 32: The "None" Trap ---')

weights = [0.12, 0.45, 0.33]
weights.append(0.77)

print(f'Updated weights: {weights}')
print('*' * 30)

# --- PROGRAM 33: WEIGHT DATA ---
print('--- Task 33: Weight Data ---')

data = [0.5, -0.2, 0.8, -0.1, 0.3, -0.9, 0.4]

positive_weights = [w for w in data if w > 0]
negative_weights = [w for w in data if w < 0]
positive_total = sum(positive_weights)

print(f'Positive weights: {positive_weights}\nTotal: {positive_total}')
print(f'Negative weights: {negative_weights}')
print('*' * 30)

# --- PROGRAM 34: LIST FROM USER ---
print('--- Task 34: List From User ---')

n = int(input('Enter the count of iterations: '))
data_list = []

for _ in range(n):
    item = input('Enter the item: ')
    data_list.append(item)

print(f'Result: {data_list}')
print('*' * 30)

# --- PROGRAM 35: CUBES OF NUMBER ---
print('--- Task 35: Cubes Of Number ---')

n = int(input('Enter the count of iterations: '))

number_cubes = [int(input('Enter the number: ')) ** 3 for _ in range(n)]

print(f'Cubes of number: {number_cubes}')
print('*' * 30)

# --- PROGRAM 36: ALL AT ONCE ---
print('--- Task 36: All At Once ---')

numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, \
           14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

print(len(numbers))
print(numbers[-1])
print(numbers[::-1])

if 5 in numbers and 17 in numbers:
    print('YES')
else:
    print('NO')

del numbers[0]
del numbers[-1]
print(numbers)

print('*' * 30)

# --- PROGRAM 37: LIST OF DIVISORS ---
print('--- Task 37: List Of Divisors ---')

n = int(input('Enter the number: '))

divisors_list = [i for i in range(1, n + 1) if n % i == 0]

print(f'Divisors list: {divisors_list}')
print('*' * 30)

# --- PROGRAM 38: SUMS OF TWO ---
print('--- Task 38: Sums Of Two ---')

n = int(input('Enter the count of numbers: '))
numbers_list = [int(input('Enter the number: ')) for number in range(n)]
sums_list = []

for i in range(n - 1):
    result = numbers_list[i] + numbers_list[i + 1]
    sums_list.append(result)

print(sums_list)
print('*' * 30)

# --- PROGRAM 39: DELETE ODD INDICES ---
print('--- Task 39: Delete Odd Indices ---')

n = int(input('Enter the count of numbers: '))
numbers_list = [int(input('Enter the number: ')) for _ in range(n)]
del numbers_list[1::2]

print(numbers_list)
print('*' * 30)

# --- Task 40: Vertical Slice ---
print('--- Task 40: Vertical Slice ---')

n = int(input('Enter the count of strings: '))

strings_list = [input('Enter the string: ') for _ in range(n)]
k = int(input('Enter index letter: '))

for s in strings_list:
    if len(s) >= k:
        print(s[k - 1], end='')

print()
print('*' * 30)