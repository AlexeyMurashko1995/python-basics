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