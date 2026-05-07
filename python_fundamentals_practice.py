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


