# --- TASK 1: Skill Capitalization Calculator ---
# This program calculates total study hours and visualizes daily progress.
print("--- Task 1: Skill Capitalization ---")
days = int(input('How many days will you be able to study? '))
total_hours = 0

for d in range(1, days + 1):
    print(f'Day {d}')
    hours = int(input('How many hours? '))
    total_hours += hours
    for h in range(hours):
        print('[#]', end=' ')
    print()  # New line after daily progress bar

print(f'Total investment in your future: {total_hours} hours.\n')


# --- TASK 2: Coordinate Grid (The Crosshair) ---
# Visualizing axes and diagonals using nested loops and linear equations.
print("--- Task 2: The Coordinate Crosshair ---")
# Grid size: 20 rows by 50 columns
for row in range(20):
    for col in range(50):
        if row == 9 and col == 25:
            print('X', end='')      # Center point (Origin)
        elif row == 9:
            print('-', end='')      # Horizontal axis
        elif col == 25:
            print('|', end='')      # Vertical axis
        elif row + col == 19:
            print('/', end='')      # Anti-diagonal (row + col = const)
        elif row - col == -31:
            print('\\', end='')     # Main diagonal (row - col = const)
        else:
            print(' ', end='')      # Empty space
    print()
print("\n")


# --- TASK 3: Diagonal Matrix (0, 1, 2 Pattern) ---
# Creating a square matrix with a secondary diagonal, upper and lower triangles.
print("--- Task 3: Diagonal Matrix Logic ---")
size = int(input('Enter the size of the square matrix: '))

for row in range(size):
    for col in range(size):
        if row + col == size - 1:
            print('1', end='\t')    # Secondary diagonal
        elif row + col > size - 1:
            print('2', end='\t')    # Lower triangle
        else:
            print('0', end='\t')    # Upper triangle
    print()