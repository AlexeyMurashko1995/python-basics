import math

# --- PROGRAM 1: DRAWING ---
print('--- Task 1: Drawing ---')

def triangle():
    for row in range(5):
        for space in range(5-row-1):
            print(' ', end='')
        for star in range(2 * row + 1):
            print('*', end='')
        print()

def rectangle():
    for row in range(5):
        for col in range(5):
            if row == 0 or col == 0 or col == 4 or row == 4:
                print('*', end='')
            else:
                print(' ', end='')
        print()

choice = int(input('What would you like to draw? 1 - triangle; 2 - rectangle: '))
if choice == 1:
    triangle()
elif choice == 2:
    rectangle()
else:
    print('Invalid input')
    
print('*' * 30) 

# --- PROGRAM 2: WATER PRICE ---
print('--- Task 2: Water Price ---')

def about_water(price):
    print('The name: ClearWater')
    print('Producer: Poland')
    print(f'Price: {price}')
    print()


about_water(25)
about_water(30)
about_water(40)
print('*' * 30)

def calculate_sphere_area(r):
    area = 4 * math.pi * (r ** 2)
    print(f'The surface area: {area:.2f}')

def calculate_sphere_volume(r):
    volume = 4 / 3 * math.pi * (r ** 3)
    print(f'The volume: {volume:.2f}')

# --- PROGRAM 3: PLANETARY CALCULATION ---
print('--- Task 3: Planetary Calculation ---')

radius = float(input('Enter the radius: '))

choice = int(input('1 - The Surface Area; 2 - The Volume: '))

if choice == 1:
    calculate_sphere_area(radius)
elif choice == 2:
    calculate_sphere_volume(radius)
else: 
    print('Invalid Input')
print('*' * 30)

# --- PROGRAM 4: PRIME NUMBER ---
print('--- Task 4: Prime Number ---')

def is_prime(n):
    divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisors += 1
            if divisors > 2:
                break
    if divisors == 2:
        return True 
    else:
        return False

amount = int(input('Enter the amount of numbers: '))

for i in range(1, amount + 1):
    current_number = int(input(f'Enter #{i} number: '))
    if is_prime(current_number):
        print('This number is a match. ')
    
print('*' * 30)

# --- PROGRAM 5: VAT CALCULATOR ---
print('--- Task 5: VAT Calculator ---')

def get_total_price(net_price):
    gross_price = net_price + (net_price * 0.23)
    return gross_price

netto = float(input('Enter net price: '))
total = get_total_price(netto)

print(f'Total price (Gross): {total:.2f}')

# --- PROGRAM 6: MAXIMUM FINDER ---
print('--- Task 6: Maximum Finder ---')

def get_max(a,b):
    if a > b:
        return a
    return b

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
print(f'Comparing {a} and {b}...')

win = get_max(a,b)

print(f'The maximum is: {win}')
print('*' * 30)

# --- PROGRAM 7: FORMATTER FUNCTION ---
print('--- Task 7: Formatter Function ---')

def get_prepare_string(text):
    clean_text = text.strip()
    final_text = clean_text.capitalize()

    return final_text

user_text = input('Enter your text: ')

print(f'Result: {get_prepare_string(user_text)}')
print('*' * 30)

# --- PROGRAM 8: THE SHOP ASSISTANT ---
print('--- Task 8: The Shop Assistant ---')

def get_discounted_price(price, discount_percent):
    if discount_percent >= 100:
        return 0.0
    final_price = price - (price * (discount_percent / 100))
    return final_price

user_price = float(input('Enter the price: '))
user_discount = int(input('Enter the discount percent: '))

total = get_discounted_price(user_price, user_discount)

print(f'Final price: {total:.2f}')
print('*' * 30)

# --- PROGRAM 9: THE ACCESS GUARD ---
print('--- Task 9: The Access Guard ---')

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False 

customer_age = int(input('Enter your age: '))

if is_adult(customer_age):
    print('Access granted')
else:
    print('Access denied')
print('*' * 30)

# --- PROGRAM 10: THE AVERAGE ---
print('--- Task 10: The Average ---')

def get_average(a,b):
    if a > b:
        return None
    return (a + b) / 2

a_1 = int(input('Enter the first number: '))
b_1 = int(input('Enter the second number: '))

result = get_average(a_1, b_1)
if result is None:
    print('Invalid Input')
else:
    print(f'Result: {result}')

print('*' * 30)




