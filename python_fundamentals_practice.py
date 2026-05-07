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
