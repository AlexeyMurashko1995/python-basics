import math

# --- PROGRAM 1: AREA OF A TRIANGLE ---
print('--- Task 1: Area of a Triangle ---')

side_a = float(input('Enter side A length: '))
side_b = float(input('Enter side B length: '))
side_c = float(input('Enter side C length: '))

# Calculating semi-perimeter
p = (side_a + side_b + side_c) / 2

# Heron's formula
area = math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))
area_rounded = round(area, 1)

print(f'Triangle area is: {area_rounded}')
print('*' * 30)

# --- PROGRAM 2: THE GAME ---
print('--- Task 2: The Game ---')

distance = float(input('Enter the distance travelled: '))
angle = int(input('Enter the angle: '))
x = 0
y = 0

angle_rad = math.radians(angle)
x = round(distance * math.cos(angle_rad), 1)
y = round(distance * math.sin(angle_rad), 1)

print(f'Current location: {x}, {y}')
print('*' * 30)

# --- PROGRAM 3: CALCULATOR ---
print('--- Task 3: Mega-Calculator ---')

user_number = float(input("Enter a number: "))

print(f"1. Floor (round down): {math.floor(user_number)}")
print(f"2. Ceiling (round up): {math.ceil(user_number)}")
print(f"3. Absolute value (abs): {abs(user_number)}")
print(f"4. Exponential (e^{user_number}): {math.exp(user_number)}")
print(f"5. Sine: {math.sin(user_number)}")
print(f"6. Cosine: {math.cos(user_number)}")

if user_number >= 0:
    print(f"7. Square root: {math.sqrt(user_number)}")
else:
    print("7. Square root: Undefined for negative numbers")

if user_number > 0:
    print(f"8. Natural logarithm (ln): {math.log(user_number)}")
    print(f"9. Base-2 logarithm: {math.log2(user_number)}")
    print(f"10. Base-10 logarithm: {math.log10(user_number)}")
else:
    print("8-10. Logarithms: Defined only for numbers > 0")

if user_number >= 0 and user_number.is_integer():
    print(f"11. Factorial: {math.factorial(int(user_number))}")
else:
    print("11. Factorial: Input is not a natural number")
print('*' * 30)

# --- PROGRAM 4: WAREHOUSE INVENTORY ---
print('--- Task 4: Warehouse Inventory ---')

name = input('Enter product name: ')
price = float(input('Enter the price: '))
quantity = input('Enter the quantity: ')

total_cost = price * int(quantity)
first_string = 'Item: '+ name + ' | ' + 'Total cost: ' + str(total_cost)
print(first_string)
second_string = 'Integer part for accounting: ' + str(int(total_cost))
print(second_string)
print('*' * 30)

# --- PROGRAM 5: THE FIRST DIGIT ---
print('--- Task 5: The First Digit ---')

number = float(input('Enter the number: '))

first_digit = (number * 10) % 10 

print(f'The first digit: {int(first_digit)}')
print('*' * 30)

# --- PROGRAM 6: VOLUME OF A PLANET ---
print('--- Task 6: Volume of a Planet ---')

radius = float(input('Enter the radius: '))

volume = 4 / 3 * math.pi * (radius ** 3)
surface = 4 * math.pi * (radius ** 2)

print(f'The volume: {volume:.2f}\nThe surface: {surface:.2f}')
print('*' * 30)

# --- PROGRAM 7: A KNIGHT'S MOVE ---
print("--- Task 7: A Knight's Move ---")

print("Enter the knight's position: ")
x = float(input(''))
y = float(input(''))

x_square = int(x * 10)
y_square = int(y * 10) 

print("Enter the target point's position: ")
x1 = float(input(''))
y1 = float(input(''))

x1_square = int(x1 * 10)
y1_square = int(y1 * 10)

if x_square > 7 or y_square > 7 or x1_square > 7 or y1_square > 7:
    print('Error: The coordinates are out of bounds (0-7).')
else:
    dx = abs(x_square - x1_square)
    dy = abs(y_square - y1_square) 

    print(f'Knight position: ({x_square}, {y_square})\nTarget position: ({x1_square}, {y1_square})')

    if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
        print('Yes, the knight can move to this point.')
    else:
        print('No, the knight cannot move to this point.')
print('*' * 30)

# --- PROGRAM 8: THE MAXIMUM OF TWO ---
print('--- Task 8: The Maximum Of Two ---')

num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the second number: '))

plus = num_1 + num_2
dif = abs(num_1 - num_2)
total = plus + dif
result = total // 2

print(result)
print('*' * 30)
