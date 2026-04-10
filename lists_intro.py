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


def get_reserved_segment(data: list, start, stop) -> list:
    return data[start:stop:][::-1]


my_list = list(range(7))
first_index = 1
last_index = 5
result = get_reserved_segment(my_list, first_index, last_index)

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