# --- PROGRAM 1: MONEY BOX ---
print('--- Task 1: Money Box ---')
n1 = int(input('How many days do you plan to save money? '))
total_savings = 0
for i in range(1, n1 + 1):
    day_money = int(input(f'How much money do you want to save on day {i}? '))
    total_savings += day_money
average = total_savings / n1 
print(f'Total savings in the money box: {total_savings}.\n Average amount saved per day: {average:.2f}.')
print('-' * 30 + '\n')

# --- PROGRAM 2: LAUNCH TIME ---
print('--- Task 2: Launch Time ---')
n2 = int(input('How many seconds before rocket launch? '))
for i in range(n2, -1, -2):
    print(f'Seconds before launch: {i}. ')
print('GO!')
print('-' * 30 + '\n')

# --- PROGRAM 3: SQUARE CALCULATOR ---
print('--- Task 3: Square Calculator ---')
n3 = int(input('Enter your number: '))
for i in range(1, n3 + 1):
    if i % 3 == 0:
        print(f'The number {i} squared: {i ** 2}.')
