# --- PROGRAM 1: STEAM DISCOUNT CALCULATOR ---
print('--- Task 1: Steam Discount Calculator ---')

total_cost = 0
discount_price = 0

quantity = int(input('How many games are in your cart? '))

for games in range(1, quantity + 1):

    game_title = input(f'Enter game #{games} name: ')
    price = float(input('Enter price: '))
    total_cost = total_cost + price

print('--- FINAL RECEIPT ---')
print(f'Total games: {quantity}\nRaw total: {total_cost:.2f} PLN')

if total_cost > 200:
    discount_price = total_cost * 0.85
    print(f'Loyalty discount applied: 15%\nFinal price: {discount_price:.2f} PLN')
else:
    print(f'Final price: {total_cost:.2f} PLN (No discount applied)')
print('*' * 30)