print("--- TASK 1: THE PIT ---")
n = int(input('Enter the size for the Pit: '))
for row in range(1, n + 1):
    for left in range(n, n - row, -1):
        print(left, end='')
    for space in range((n - row) * 2):
        print('.', end='')
    for right in range(n - row + 1, n + 1):
        print(right, end='')
    print()

print("\n" + "="*20 + "\n") 

print("--- TASK 2: SANDGLASS ---")
n = int(input('Enter the size for Sandglass: '))

for row in range(n, 0, -1):
    for space in range(n - row):
        print(' ', end='')
    for star in range(2 * row - 1):
        print('*', end='')
    print()

for row in range(2, n + 1):
    for space in range(n - row):
        print(' ', end='')
    for star in range(2 * row - 1):
        print('*', end='')
    print()

print("\n" + "="*20 + "\n")

print("--- TASK 3: NUMBER PYRAMID ---")
number = int(input('Enter the size for Pyramid: '))
num_counter = 1
for row in range(1, number + 1):
    for space in range(number - row):
        print(' ', end='\t')
    for num in range(row):
        print(num_counter, end='\t\t')
        num_counter += 2
    print()