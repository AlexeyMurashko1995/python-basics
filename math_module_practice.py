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

# --- PROGRAM 3: MEGA-CALCULATOR ---
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