# --- PROGRAM 1: DICTIONARY CRUD AND LOGIC ---
print('--- Task 1: Dictionary CRUD And Logic ---')

flat_info = {
    'city': 'Warsaw',
    'flat_type': 'apartment',
    'price per meter': 19000,
    'area': 49.6
}

flat_info['price per meter'] = flat_info['price per meter'] + (flat_info['price per meter'] * 0.1)
flat_info['is_expensive'] = flat_info['price per meter'] > 15000

print(flat_info)
print('*' * 30)