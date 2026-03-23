# Task 1: Exercise timer with reverse countdown
# Demonstrates nested loops and range steps
print("--- Task 1: Timer ---")
for ex in range(1, 3):
    print(f'Exercise {ex}')
    for time in range(3, 0, -1):
        print(f'Remaining: {time} seconds')
    print('---')

# Task 2: Multiplier table with even-only filter
# Shows how to use 'continue' and modulo operator
print("\n--- Task 2: Even Multipliers ---")
for i in range(1, 3):
    for j in range(1, 6):
        product = i * j
        if product % 2 == 0:
            print(product)
        else:
            continue

# Task 3: Warehouse inventory (Odd cartons only)
# Using != operator to filter specific data
print("\n--- Task 3: Warehouse Analytics ---")
for item_type in range(1, 3):
    print(f'Item Type {item_type}:')
    for carton in range(1, 5):
        if carton % 2 != 0:
            print(f'Carton #{carton}')
    print('---')

# Task 4: Pattern Matrix (The "Black Box" logic)
# Logic: If column is divisible by 3, print column, else print row
print("\n--- Task 4: Pattern Matrix ---")
n = 6
for row in range(1, n + 1):
    for col in range(1, n + 1):
        if col % 3 == 0:
            print(col, end='\t')
        else:
            print(row, end='\t')
    print()

# Task 5: Coordinate System Visualization
# Demonstrates condition priority (If-Elif-Else)
print("\n--- Task 5: Coordinate Axis ---")
for row in range(20):
    for col in range(50):
        if row == 9 and col == 25:
            print('+', end='')  # Intersection point
        elif row == 9:
            print('-', end='')  # Horizontal axis
        elif col == 25:
            print('|', end='')  # Vertical axis
        else:
            print(' ', end='')  # Empty space
    print()