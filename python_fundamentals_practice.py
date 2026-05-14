from collections import deque

# ==============================================================================
# TASK 1: NUMBER REVERSAL
# ==============================================================================
# print('--- Task 1: Number Reversal ---')
# user_number = str(int(input()))
#
# if len(user_number) == 6:
#     prefix = user_number[0:1]
#     reverse = user_number[-1:0:-1]
#     result = int(prefix + reverse)
# else:
#     result = int(user_number[::-1])
#
# print(result)
# print('*' * 30)


# ==============================================================================
# TASK 6: JOSEPHUS PROBLEM
# ==============================================================================
# print('--- Task 6: Josephus Problem ---')
# n = int(input(''))
# k = int(input(''))
#
# people_list = list(range(1, n + 1))
# index = 0
#
# while len(people_list) > 1:
#     i = (index + k - 1) % len(people_list)
#     people_list.pop(i)
#     index = i
#
# print(people_list[0])
# print('*' * 30)


# ==============================================================================
# TASK 10: LIST ROTATION (Standard method)
# ==============================================================================
# print('--- Task 10: List Rotation ---')
# number_list = [int(x) for x in input().split()]
#
# last_digit = number_list.pop()
# number_list.insert(0, last_digit)
#
# print(*number_list)
# print('*' * 30)


# ==============================================================================
# TASK 10: LIST ROTATION (Using class deque)
# ==============================================================================
print('--- Task 10: List Rotation (using class deque) ---')

number_list = [int(x) for x in input().split()]

dq_list = deque(number_list)
dq_list.rotate(1)

print(*dq_list)
print('*' * 30)