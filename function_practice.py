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