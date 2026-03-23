# --- PROGRAM 1: CUBES OF EVEN NUMBERS ---
print("--- Task 1: Cubes of Even Numbers ---")
n1 = int(input('Enter a number: '))
for i in range(1, n1 // 2 + 1):
    i *= 2
    print(f'Number {i} cubed is: {i ** 3}')
print("-" * 30 + "\n")

# --- PROGRAM 2: AMOEBA DIVISION ---
print("--- Task 2: Amoeba Division Simulation ---")
time = int(input('Enter the number of hours for observation: '))
time_remaining = time
cells = 1
for i in range(1, time // 3 + 1):
    time_remaining -= 3
    cells *= 2
    print(f'Hours passed: {i * 3}')
    print(f'Time remaining: {time_remaining} hours')
    print(f'Number of cells: {cells}')
    print()

print('Observation complete.')
print("-" * 30 + "\n")

# --- PROGRAM 3: SQUARES OF ODD NUMBERS ---
print("--- Task 3: Squares of Odd Numbers ---")
n3 = int(input('Enter any number: '))
for i in range(1, n3 + 1, 2):
    print(f'The result of squaring {i} is: {i ** 2}')