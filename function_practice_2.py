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

