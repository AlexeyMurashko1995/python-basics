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