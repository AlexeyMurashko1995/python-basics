# --- PROGRAM 1: DATA SCALING ---
print('--- Task 1: Data Scaling ---')

def scale_value(scale, value):
    result = scale * value
    return result 

init_value = float(input('Enter the initial value: '))
weight = float(input('Enter weight: '))
total = scale_value(init_value, weight)
print(f'Resulting scale: {total}')
print('*' * 30)

# --- PROGRAM 2: PROMPT CLEANING ---
print('--- Task 2: Prompt Cleaning ---')

def clean_prompt(text): 
    clean_text = text.strip()
    final_text = clean_text.capitalize()
    return final_text

raw_prompt = input('Enter the raw prompt: ')
cleaned_version = clean_prompt(raw_prompt)

print(f'Cleaned version: {cleaned_version}')
print('*' * 30)

# --- PROGRAM 3: ACTIVATION THRESHOLD ---
print('--- Task 3: Activation Threshold ---')

def is_activated(score): 
    return score > 0.5

probability_score = float(input('Enter probability score: '))

status = is_activated(probability_score)

if status:
    print('Neuron status: True')
else:
    print('Neuron status: False')
print('*' * 30)

# --- PROGRAM 4: INPUT VALIDATION ---
print('--- Task 4: Input Validation ---')

def is_valid_input(text):
    return text.strip() != '' and len(text) > 3
    

prompt = input('Enter the phrase: ')
valid = is_valid_input(prompt)

if valid:
    print('Is valid: True')

else:
    print('Is valid: False')
print('*' * 30)

# --- PROGRAM 5: RELIABLE PREDICTION ---
print('--- Task 5: Reliable Prediction ---')

def is_reliable(confidence, min_threshold):
    return confidence >= min_threshold 

ai_confidence = float(input('Enter AI confidence (0.0 - 1.0): '))
minimum_threshold = float(input('Enter minimum threshold: '))

reliability_status = is_reliable(ai_confidence, minimum_threshold)

if reliability_status:
    print('Reliability status: True')

else:
    print('Reliability status: False')
print('*' * 30)    

# --- PROGRAM 6: GREATEST COMMON DIVISOR ---
print('--- Task 6: Greatest Common Divisor ---')

def greatest_common_divisor(a, b):
    # In this function, I use the Euclidean algorithm to find the greatest common divisor
    while b: 
        a, b = b, a % b
    return a 


first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))

result = greatest_common_divisor(first_number, second_number)
print(result)
print('*' * 30)

# --- PROGRAM 7: FIBONACCI SEQUENCE ---
print('--- Task 7: Fibonacci Sequence ---')

def get_sequence_fibonacci(number):
    a, b = 0, 1
    result = []
    for num in range(number):
        result.append(a)
        a, b = b, a + b
    return result
        
quantity = int(input('Enter the number of elements: '))
final = get_sequence_fibonacci(quantity)
print(final)
print('*' * 30)

# --- PROGRAM 8: ACCESS CONTROL LIST (ACL) ---
print('--- Task 8: Access Control List ---')

def get_access_list(name):
    reject = ['admin', 'root', 'superuser']
    return name.lower() in reject
    

user_name = input('Enter username: ')

status = get_access_list(user_name)
if status:
    print('Access Denied: This account is restricted.')
else:
    print('Access Granted: Welcome back!')
print('*' * 30)

# --- PROGRAM 9: POWER OF TWO ---
print('--- Task 9: Power Of Two ---')

def is_power_of_two(num):
    if num <= 0:
        return False 
    while num % 2 == 0:
        num //= 2
    return num == 1  
        
number = int(input('Enter the number: '))

result = is_power_of_two(number)
if result:
  print('Result: True')
else:
  print('Result: False')
print('*' * 30)
    
# --- PROGRAM 10: FIZZBUZZ CLASSIC ---
print('--- Task 10: FizzBuzz Classic')

def get_fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('Fizzbuzz')
        elif i % 3 == 0: 
            print('Fizz') 
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
   
    
num = int(input('Enter the range: '))
get_fizzbuzz(num)
print('*' * 30)

# --- PROGRAM 11: THE SUM OF NUMBERS ---
print('--- Task 11: The Sum Of Numbers ---')

def get_sum_numbers(num):
    #Applying the Gaussian summation formula here.
    return (num * (num + 1) // 2)


number = int(input('Enter the number: '))

result = get_sum_numbers(number)
print(f'The sum from 1 to {number}: {result}')

final_result = get_sum_numbers(result)
print(f'The sum from 1 to {result}: {final_result}')
print('*' * 30)

# --- PROGRAM 12: BACK TO THE FUTURE ---
print('--- Task 12: Back To The Future ---')

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))    
result = get_gcd(first_number, second_number)

print(f'The great common divisor: {result}')
print('*' * 30)

    
    



   
