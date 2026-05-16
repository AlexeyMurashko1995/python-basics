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


# ==============================================================================
# TASK 11: ZIP CODE RANGE GENERATOR
# ==============================================================================
# print('--- Task 11: Zip Code Range Generator ---')

# first_index = input().replace('-', '')
# second_index = input().replace('-', '')

# first_index = int(first_index)
# second_index = int(second_index)

# if first_index < second_index:
#     indexes_list = []

#     for number in range(first_index + 1, second_index):
#         number = str(number)
#         index = number[:2] + '-' + number[2:]
#         indexes_list.append(index)

#     print(*indexes_list)
# else:
#     print('The second index must be greater than first')
# print('*' * 30)

# ==============================================================================
# Task 12. FINDING MISSING ELEMENTS (First Variant)
# ==============================================================================

def get_missing_numbers(n: int, number_list: list) -> list:
    missing_list = [number for number in range(1, n + 1) if number not in number_list]
    return missing_list

user_range = int(input())
user_list = [int(y) for y in input().split(' ')]

result = get_missing_numbers(user_range, user_list)

print(*result)
