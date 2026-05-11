# --- TASK 1: NUMBER REVERSAL ---
print('--- Task 1: Number Reversal ---')

user_number = int(input())
user_number = str(user_number)

if len(user_number) == 6:
    prefix = user_number[0:1:]
    reverse = user_number[-1:0:-1]
    result = int(prefix + reverse)

else:
    result = int(user_number[::-1])

print(result)
print('*' * 30)

# --- TASK 2: CREDIT CARD MASKING ---
print('--- Task 2: Credit Card Masking ---')

user_card = int(input())
user_card = str(user_card)

user_card_feat = '*' * 12 + user_card[12:]

print(user_card_feat)
print('*' * 30)

# --- TASK 3: TASK 3: REVERSED NAME BRANDING ---
print('--- Task 3: Reverse Name Branding ---')

user_input = input().lower()

first_letter = user_input[:1].capitalize()
reverse = user_input [-1:0:-1]

print(first_letter + reverse)
print('*' * 30)

# --- TASK 4: DYNAMIC STRING SPLIT & SWAP ---
print('--- Task 4: Dynamic String Split & Swap ---')

user_input = input()

if len(user_input) % 2 == 0:
    first_half = user_input[len(user_input) // 2:]
    second_half = user_input[:len(user_input) // 2]
    filtered_output = first_half + second_half
else:
    filtered_output = user_input

print(filtered_output)
print('*' * 30)

# --- TASK 5: STANDARD AMERICAN CONVENTION ---
print('--- Task 5: Standard American Convention ---')

user_input = int(input())
user_input = str(user_input)

result = []

while len(user_input) > 3:
    result.append(user_input[-3:])
    user_input = user_input[:-3]

result.append(user_input)
result.reverse()

print(','.join(result))
print('*' * 30)

# --- TASK 6: JOSEPHUS PROBLEM ---
print('--- Task 6: Josephus Problem ---')

n = int(input(''))
k = int(input(''))

people_list = list(range(1,n + 1))
index = 0

while len(people_list) > 1:
    i = (index + k - 1) % len(people_list)
    people_list.pop(i)
    index = i

print(people_list[0])
print('*' * 30)

# --- TASK 7: COORDINATE QUADRANTS ---
print('--- Task 7: Coordinate Quadrants ---')

n = int(input(''))

first_quadrant = 0
second_quadrant = 0
third_quadrant = 0
fourth_quadrant = 0

for _ in range(n):
    number_list = [int(x) for x in input('').split(' ')]
    x = number_list[0]
    y = number_list[1]
    if x > 0 and y > 0:
        first_quadrant += 1
    elif x < 0 and y > 0:
        second_quadrant += 1
    elif x < 0 and y < 0:
        third_quadrant += 1
    elif x > 0 and y < 0:
        fourth_quadrant += 1

print(f'First quadrant: {first_quadrant}')
print(f'Second quadrant: {second_quadrant}')
print(f'Third quadrant: {third_quadrant}')
print(f'Fourth quadrant: {fourth_quadrant}')

print('*' * 30)

# --- TASK 8: GREATER THAN THE PREVIOUS ONE ---
print('--- Task 8: Greater Than The Previous One ---')

# First variant
number_list = [int(x) for x in input().split()]

count = -1
temp_number = -1

for number in number_list:
    if number > temp_number:
        count += 1
    temp_number = number
print(count)

#Second variant
number_list = [int(x) for x in input().split()]

count = 0

for i in range(1, len(number_list)):
    if number_list[i] > number_list[i - 1]:
        count += 1

print(count)
print('*' * 30)

# --- TASK 9: BACK AND FORTH ---
print('--- Task 9: Back And Forth ---')

number_list = [int(x) for x in input().split()]

for i in range(0, len(number_list) - 1, +2):
    number_list[i],number_list[i + 1] = number_list[i + 1], number_list[i]

print(*number_list)
print('*' * 30)