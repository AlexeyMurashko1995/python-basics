# Part 1: Prime Numbers Search
print("--- Task 1: Prime Numbers Search ---")
quantity = int(input('How many numbers to investigate: '))
prime_count = 0

for num in range(1, quantity + 1):
    number = int(input(f'Enter number {num}: '))
    divisors = 0
    
    # Checking for divisors
    for div in range(1, number + 1):
        if number % div == 0:
            divisors += 1
            
    # A prime number has exactly 2 divisors (1 and itself)
    if divisors == 2:
        prime_count += 1

print(f'Total prime numbers in the sequence: {prime_count}\n')


# Part 2: Odd Number Pyramid
print("--- Task 2: Odd Number Pyramid ---")
height = int(input('Enter the height of the triangle: '))
current_number = 1

for row in range(1, height + 1):
    # 1. Printing leading spaces for alignment
    for space in range(height - row):
        print(' ', end='\t')
        
    # 2. Printing odd numbers (the count matches the row number)
    for col in range(row):
        print(current_number, end='\t\t')
        current_number += 2 # Move to the next odd number
        
    print() # New line after each row