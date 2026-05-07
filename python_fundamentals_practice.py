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