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