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

# --- PROGRAM 13: TASK PRIORITY ---
print('--- Task 13: Task Priority ---')

def numeral_count(num):
    num = abs(num)
    if num == 0:
        return 1
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count


amount = int(input('Enter the amount of tasks: '))

digits_max = 0
number_win = 0

for tasks in range(1, amount + 1):
    number = int(input(f'Enter the #{tasks} task number: '))
    result = numeral_count(number)
    if result > digits_max:
        digits_max = result
        number_win = number
print(f'The most digits - {digits_max}; task number: {number_win}')
print('*' * 30)

# --- PROGRAM 14: AI ACCURACY CHECKER ---
print('--- Task 14: AI Accuracy Checker ---')

def get_model_accuracy(results_list):
    correct_count = 0
    for prediction in results_list:
        if prediction == 1:
            correct_count += 1
    result = correct_count / len(results_list) * 100
    return result

predictions = [1, 1, 0, 1, 0, 1]
model_accuracy = get_model_accuracy(predictions)
print(f'Model accuracy: {model_accuracy:.2f}% ')

# --- PROGRAM 15: COMPARISON OF PREDICTIONS ---
print('--- Task 15: Comparison Of Predictions ---')

def get_match_count(actual_list, predicted_list):
    if len(actual_list) != len(predicted_list):
        print('Error: Lists have different lengths!')
        return 0
    count = 0
    for i in range(len(actual_list)):
        if actual_list[i] == predicted_list[i]:
            count += 1
    return count

ground_truth = [1, 0, 1, 1, 0]
predictions = [1, 1, 1, 0, 0]
result = get_match_count(ground_truth, predictions)

print(f'Identical values: {result}')
print('*' * 30)

# --- PROGRAM 16: ANOMALY DETECTOR ---
print('--- Task 16: Anomaly Detector ---')

def find_anomalies(data):
    filtered_readings = []
    for i in data:
        if i > 80:
            filtered_readings.append(i)
    return filtered_readings

sensor_readings = [72, 85, 79, 92, 90, 68, 81]
anomalies_detected = find_anomalies(sensor_readings)

print(f'Detected anomalies: {anomalies_detected}')
print('*' * 30)

# --- PROGRAM 17: ANOMALY INDEXER ---
print('--- Task 17: Anomaly Indexer ---')


def get_anomaly_indices(data, threshold):
    index_list = []
    for index, value in enumerate(data):
        if value > threshold:
            index_list.append(index)
    return index_list


sensor_readings = [72, 95, 94, 123, 43, 90, 12, 141]
user_threshold = int(input('Enter threshold: '))

anomaly_indexer = get_anomaly_indices(sensor_readings, user_threshold)
print(f'Indices of anomalies: {anomaly_indexer}')
print('*' * 30)

# --- PROGRAM 18: FIND THE PEAK (MAX VALUE) ---
print('--- Task 18: Find The Peak: Max Value ---')


def find_max_score(data):
    value_max = data[0]
    for value in data:
        if value > value_max:
            value_max = value
    return value_max


data_list = [0.45, 0.99, 0.12, 0.87, 0.98]
max_value = find_max_score(data_list)

print(f'The higher score is {max_value}')
print('*' * 30)

# --- PROGRAM 19: SIGNAL INTEGRATOR ---
print('--- Task 19: Signal Integrator ---')


def sum_signals(data):
    total = 0
    for signal in data:
        total += signal
    return total


signals = [1.5, 2.0, -0.5, 3.0]
final_result = sum_signals(signals)

print(f'The sum of signals is {final_result}')
print('*' * 30)

# --- PROGRAM 20: SHORT STRING FILTER ---
print('--- Task 20: Short String Filter ---')


def get_short_strings(string_list, max_length):
    filtered_list = []
    for word in string_list:
        if len(word) <= max_length:
            filtered_list.append(word)
    return filtered_list


words = ['python', 'c', 'java', 'go', 'javascript', 'ruby', 'php']
limit = int(input('Enter the limit: '))
short_list = get_short_strings(words, limit)

print(f'Short words: {short_list}')
print('*' * 30)

# --- PROGRAM 21: DIGITAL COMPLEXITY ANALYZER ---
print('--- Task 21: Digital Complexity Analyzer ---')


def digit_sum(num):
    num = abs(num)
    total = 0
    while num > 0:
        last_digit = num % 10
        total += last_digit
        num //= 10
    return total


amount = int(input('Enter the quantity of tasks: '))
digits_win = 0
task_win = 0

for i in range(1, amount + 1):
    number = int(input(f'Enter the #{i} task number: '))
    result = digit_sum(number)
    if result > digits_win:
        digits_win = result
        task_win = number

print(f'The most difficult task: {task_win};\nThe sum of digits: {digits_win}')
print('*' * 30)

# --- PROGRAM 22: NUMBER NORMALIZER ---
print('--- Task 22: Number Normalizer ---')


def get_num_exp(x):
    if x <= 10:
        return False

    iteration = 0
    while x >= 10:
        x /= 10
        iteration += 1
    result = f'x = {x} * 10 ** {iteration}'
    return result


number = float(input('Enter the number greater than 10: '))
status = get_num_exp(number)

if status is False:
    print('Invalid Input')
else:
    print(status)
print('*' * 30)

# --- PROGRAM 23: TAXES ---


import math


print('--- Task 23: Taxes ---')


def get_diff(tax, new_tax):
    total = tax + new_tax
    filtered_total = math.floor(math.log10(total))
    filtered_tax = math.floor(math.log10(tax))
    if filtered_tax != filtered_total:
        return True
    else:
        return False


country_tax = float(input('Enter the budget: '))
new_country_tax = float(input('Enter the sum of new taxes: '))

status = get_diff(country_tax, new_country_tax)

if status:
    print('The budget will increase')
else:
    print('The budget will not increase')

# --- PROGRAM 24: COMPARISON ---
print('--- Program 24: Comparison ---')


def get_eqv(a,b,c):
    d = a + b
    if abs(c - d) < 1e-15:
        return True
    return False


first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))
third_number = float(input('Enter the third number: '))
result = get_eqv(first_number, second_number, third_number)

if result:
    print('True')
else:
    print('False')
print('*' * 30)

# --- PROGRAM 25: PACKAGING CONTROL ---
print('--- Task 25: Packaging Control ---')


def get_compare_weights(weight, amount, expected_weight):
    fact_weight = 0
    for portion in range(amount):
        fact_weight += weight
    return abs(expected_weight - fact_weight) <= 1e-15


user_weight = float(input('Enter the weight of one portion: '))
user_amount = int(input('Enter the quantity of portions: '))
user_expected_weight = float(input('Enter expected total weight: '))

result = get_compare_weights(user_weight, user_amount, user_expected_weight)

if result:
    print('True: Weights Match')
else:
    print("False: Weights don't match")
print('*' * 30)

# --- PROGRAM 26: MAXIMUM OF THREE ---
print('--- Task 26: Maximum Of Three ---')


def maximum_of_two(a, b):
    return ((a + b) + abs(a - b)) / 2


def maximum_of_three(a, b, c):
    max_of_first_two = maximum_of_two(a,b)
    return maximum_of_two(max_of_first_two, c)



first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
third_number = int(input('Enter the third number: '))

result = int(maximum_of_three(first_number, second_number, third_number))

print(f'The greatest number: {result}')
print('*' * 30)