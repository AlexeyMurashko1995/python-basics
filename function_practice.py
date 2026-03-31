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

# --- PROGRAM 11: GPS-NAVIGATOR ---
print('--- Task 11: GPS-Navigator ---')

def get_customer_distance(x,y):
    distance = math.sqrt((x ** 2) + (y ** 2))
    return distance

def get_between_points(x_1, y_1, x_2, y_2):
    distance_2 = math.sqrt(((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2))
    return distance_2

choice = int(input('1 - Find the distance from your location to the point; 2 - Find the distance between two points: '))

if choice == 1:
    x = float(input('Enter the X coordinate: '))
    y = float(input('Enter the Y coordinate: '))
    result = get_customer_distance(x, y)
    print(f'The distance: {result:.2f}')

elif choice == 2: 
    x_1 = float(input('Enter the coordinate X for the first point: '))
    y_1 = float(input('Enter the coordinate Y for the first point: '))
    x_2 = float(input('Enter the coordinate X for the second point: '))
    y_2 = float(input('Enter the coordinate Y for the second point: '))
    result_2 = get_between_points(x_1, y_1, x_2, y_2)
    print(f'The distance: {result_2:.2f}')

else:
    print('Invalid Input')

print('*' * 30)

# --- PROGRAM 12: THE SUM OF NUMBERS ---
print('--- Task 12: The Sum Of Numbers ---')

def get_sum_numbers(n):
    if n < 1:
        return None
    total = 0
    for i in range (1, n + 1):
        total += i
    return total

number = int(input('Enter the number: '))

total_sum = get_sum_numbers(number)

if total_sum is None:
    print('The number must be higher than 0')
else:
    print(f'The sum of numbers from 1 to {number}: {total_sum}')

print('*' * 30)

# --- PROGRAM 13: NESTED FUNCTION ---
print('--- Task 13: Nested Function ---')

def positive():
    print('Positive')

def negative():
    print('Negative')

def test():
    number = int(input('Enter the number: '))
    if number > 0: 
        positive()
    elif number < 0:
        negative()
    elif number == 0:
        print('Invalid Input')

test()

print('*' * 30)

# --- PROGRAM 14: UPGRADE CALCULATOR ---
print('--- Task 14: Upgrade Calculator ---')

def get_sum_digits(n):
    total = 0
    if n == 0:
        return 0
    while n > 0:
        last_digit = n % 10
        total += last_digit
        n //= 10
    return total

def get_min_number(n):
    min = 9
    if n == 0:
        return 0
    while n > 0:
        last_digit = n % 10
        if last_digit < min:
            min = last_digit
        n //= 10
    return min

def get_max_number(n):
    max = 0
    if n == 0:
        return 0
    while n > 0:
        last_digit = n % 10
        if last_digit > max:
            max = last_digit
        n //= 10
    return max
        
is_running = True 
while is_running: 
    number = int(input('\nEnter the number (or -1 to exit): '))

    if number == -1:
        print('Work finished.')
        is_running = False

    else: 

        choice = int(input('Choose the action: 1 - the sum of numbers; 2 - min number; 3 - max number: '))

        if choice == 1:
            result = get_sum_digits(number)
            print(f'The sum of digits: {result}')

        elif choice == 2: 
            result = get_min_number(number)
            print(f'The minimum: {result}')

        elif choice == 3:
            result = get_max_number(number)
            print(f'The maximum: {result}')

        else:
            print('Invalid Input')
print('*' * 30)

# --- PROGRAM 15: MULTI-GAME MINI APP ---
print('--- Task 15: Multi-Game Mini App ---')

def play_rock_paper_scissors(user_choice):
    computer_choice = 'Rock'
    print(f'Computer chose: {computer_choice}')
    
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Rock' and computer_choice == 'Scissors'):
        print('Congratulations! You won!')
    else:
        print('You lost! Better luck next time.')

def process_guess(user_number, secret_number):
    if user_number < secret_number:
        print('The hidden number is greater than your guess.')
    elif user_number > secret_number:
        print('The hidden number is less than your guess.')
    else:
        print('Perfect! You guessed the number!')

def start_main_menu():
    user_name = input('Please enter your name: ')
    print(f'Hello, {user_name}! Welcome to the Mini-Game App.')
    
    is_active = True
    while is_active:
        print('\n--- MAIN MENU ---')
        print('1 - Play Rock, Paper, Scissors')
        print('2 - Play Guess the Number')
        print('0 - Exit')
        
        menu_selection = int(input('Please select an option: '))
        
        if menu_selection == 1:
            move = input('Enter your move (Rock, Paper, or Scissors): ')
            play_rock_paper_scissors(move)
            
        elif menu_selection == 2:
            target_number = 77 
            print("I've thought of a number between 1 and 100. Try to guess it!")
            
            current_guess = 0
            while current_guess != target_number:
                current_guess = int(input('Enter your guess: '))
                process_guess(current_guess, target_number)
                
        elif menu_selection == 0:
            print('Thank you for playing! Goodbye.')
            is_active = False
        else:
            print('Invalid selection. Please try again.')

start_main_menu()

print('*' * 30)

# --- PROGRAM 16: TEXT EDITOR ---
print('--- Task 16: Text Editor ---')

def get_count_letters(phrase, our_digit, our_letter):
    digit = 0
    letter = 0
    
    for char in phrase:
        if char == our_digit:
            digit += 1
        elif char.lower() == our_letter:
            letter += 1 
    print(f'The amount of "{our_digit}": {digit}\nThe amount of "{our_letter}": {letter}')


text = input('Enter the text: ')
digit_to_find = input('Which digit are we looking for? ')
letter_to_find = input('Which letter are we looking for: ').lower()
get_count_letters(text, digit_to_find, letter_to_find)
print('*' * 30)
