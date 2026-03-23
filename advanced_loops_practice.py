#1 --- PROGRAM 1: DEBTOR DATABASE --- 
print('--- Task 1: Debtor Database ---')
debtor_count = int(input('Enter the count of debtors: '))
total_balance = 0
for i in range(0, debtor_count, 5):
    debtor_amount = int(input(f'Enter the amount of debtor №{i}: '))
    total_balance += debtor_amount
print(f'Total debt is {total_balance}.')
print('-' * 30 + '\n')

#2 --- PROGRAM 2: SPACE FOOD ---
print('--- Task 2: Space Food ---')
food_supply = int(input('Enter the food supply in kilograms: '))
months = 0
for food_left in range(food_supply, -1, -4):
        print(f'Month №{months}. Food remaining: {food_left}.')
        months += 1
print(f'The food ran out after {months} months.')
print('-' * 30 + '\n')

#3 --- PROGRAM 3: FUNCTION CALCULATOR ---
print('--- Task 3: Function y = -x**2 + 1 ---')
start = int(input('Enter start: '))
finish = int(input('Enter end: '))
step = int(input('Enter step: '))
for x in range(start, finish + 1, step):
    y = -(x ** 2) + 1
    print(f'At x = {x}, y = {y}')
print('-' * 30 + '\n')

#4 --- PROGRAM 4:SCHOLARSHIP ---
print('--- Task 4: Scholarship ---')
scholarship = int(input('Enter the amount of your scholarship: '))
expenses = int(input('Enter the expense amount: '))
total_expenses = 0
study_duration = 10
total_scholarship = scholarship * study_duration
for month in range (1, study_duration + 1):
    print(f'{month} months later.\n Your expenses: {expenses}.')
    total_expenses += expenses
    expenses = expenses + (3 * expenses // 100)
print(f'The total amount spent over {month} months of study: {total_expenses}.')
print(f'You are short by the following amount: {total_expenses - total_scholarship}.')
print(f'Amount to ask parents for: {total_expenses - total_scholarship}.')