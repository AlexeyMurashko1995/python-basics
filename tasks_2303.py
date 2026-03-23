# #--- TASK 1: SPACE RANGERS ---
print('--- Task 1: Space ---')
money = int(input('Enter the amount of chattles: '))

CR = float(money / 2200)
ship_price = 0.5
space_ship = int(CR / ship_price)

print(f'You have {CR} CR')
print(f'You can buy: {space_ship} space ships')
print('*' * 20)

#--- TASK 2: CHESSBOARD ---
print('--- Task 2: Chessboard ---')
print(f'Enter the piece location: ')
x = float(input('Enter a number horizontally: '))
y = float(input('Enter a number vertically: '))



x_square = int(x * 10)
x_ideal = (x_square * 0.1) + 0.05
dif_x = round(x_ideal - x, 3)
y_square = int(y * 10)
y_ideal = (y_square * 0.1) + 0.05
dif_y = round(y_ideal - y, 3)

if x_square > 7 or y_square > 7 or x_square < 0 or y_square < 0:
    print('This coordinate does not exist! ')
else:
    print(f'The piece is at ({x_square}, {y_square})')
    print(f'Adjust the piece position to ({dif_x}, {dif_y})')
print('*' * 20)




