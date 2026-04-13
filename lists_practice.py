# --- PROGRAM 1: APARTMENT INDEXING ---
print('--- Task 1: Apartment Indexing ---')

apartment_1 = ["Mokotow", 45, 600000]
apartment_2 = ["Wola", 38, 520000]
apartment_3 = ["Praga", 50, 480000]

apartments = [
    apartment_1,
    apartment_2,
    apartment_3
]

print(apartments[1][2])
print('*' * 30)

# --- PROGRAM 2: PRICE FILTER ---
print('--- Task 2: Price Filter ---')

prices = [550000, 720000, 480000, 950000, 610000]
expensive_apartments = []

for price in prices:
    if price > 600000:
        expensive_apartments.append(price)

print(expensive_apartments)
print('*' * 30)

# --- PROGRAM 3: DISTRICT RENT FORMATTER ---
print('--- Task 3: District Rent Formatter ---')

rent_data = [["Wola", 3500], ["Bialoleka", 2800], ["Praga", 3200]]

for district, price in rent_data:
    print(f'The rent in {district} is {price} PLN')

print('*' * 30)

# --- PROGRAM 4: NESTED LIST ITERATION ---
print('--- Task 4: Nested List Iteration ---')

data = [["Mokotow", 45], ["Wola", 38], ["Bemowo", 50]]

for district, total_area in data:
    if total_area > 40:
        print(f'Large apartment in {district}')
    else:
        print(f'Total area: {total_area}')

print('*' * 30)