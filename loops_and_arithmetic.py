# --- PROGRAM 1: IP Address ---
print('--- Task 1: IP Address ---')
number = int(input('Enter the first number: '))
step = int(input('Enter the step: '))
total = 0

print(f'IP-address: ', end='')
for i in range(3):
    print(number, end='.')
    total += number
    number += step
print(total)
print('-' * 10)

# --- PROGRAM 2: Scoreboard ---
print('--- Task 2: Scoreboard ---')
limit = int(input('Enter the maximum score: '))

if limit < 0:
    print('The number must be greater than zero.')
else:
    # Your nested loop logic
    for n in range(1):
        print('-=-', end=' ')
        for i in range(0, limit + 1, 10):
            print(i, end=' ')
            for l in range(1):
                print('-=-', end=' ')
    print() # To move to a new line at the end