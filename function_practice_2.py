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