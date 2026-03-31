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
