# --- TASK 1: Queue Service Simulation ---
# Simulates a queue where the number of customers decreases every hour.
print("--- Task 1: Queue Simulation ---")
people_count = int(input('Enter the number of people in the queue: '))

for hour in range(1, people_count + 1):
    print(f'\nProcessing hour {hour}:')
    for person_index in range(hour - 1, people_count):
        print(f'Customer ID in line: {person_index}')
    print('-' * 20)
print('Status: All customers served!\n')


# --- TASK 2: Tabulated Offset Ladder ---
# Generates a matrix where each row starts with an incremented index.
print("--- Task 2: Offset Table ---")
limit = int(input('Enter a limit number for the table: '))

for row in range(limit + 1):
    for col in range(row, limit):
        print(col, end='\t')
    print()
print("\nTable generated successfully.\n")


# --- TASK 3: Hollow Rectangle (The Frame) ---
# Draws a frame using coordinate logic (borders vs. empty space).
print("--- Task 3: Drawing a Frame ---")
height = int(input('Enter the height: '))
width = int(input('Enter the width: '))

for row in range(height):
    for col in range(width):
        if col == 0 or col == width - 1:
            print('|', end='')
        elif row == 0 or row == height - 1:
            print('-', end='')
        else:
            print(' ', end='')
    print()
print("\nFrame rendered.\n")


# --- TASK 4: Prime Number Counter (Custom Logic) ---
# Counts numbers with 2 or fewer divisors (including number 1).
print("--- Task 4: Prime Number Counter ---")
quantity = int(input('How many numbers would you like to check? '))

while quantity <= 0:
    quantity = int(input('Error: Enter a number 1 or greater: '))

prime_count = 0

for i in range(1, quantity + 1):
    number = int(input(f'Enter number #{i}: '))
    dividers = 0 
    
    for check in range(1, number + 1):
        if number % check == 0:
            dividers += 1
    
    # Custom logic: counting numbers with 2 or fewer divisors
    if dividers <= 2:
        prime_count += 1

print(f'\nFinal Result: Found {prime_count} "prime-ish" numbers.')