# -------------------------------
# Task 1.
# -------------------------------


# def count_to_three():
#     yield '1'
#     yield '2'
#     yield '3'


# result = count_to_three()
# print(result)

# -------------------------------
# Task 2.
# -------------------------------


# def count_to_three():
#     yield '1'
#     yield '2'
#     yield '3'

# result = count_to_three()

# print(next(result))
# print(next(result))
# print(next(result))

# -------------------------------
# Task 3.
# -------------------------------

# def count_to_three():
#     yield '1'
#     yield '2'
#     yield '3'


# result = count_to_three()

# for string in result:
#     print(string)

# -------------------------------
# Task 4.
# -------------------------------

# def custom_range(n):
#     for number in range(1, n + 1):
#         yield number


# result = custom_range(5)

# for value in result:
#     print(value)

# -------------------------------
# Task 5.
# -------------------------------

# def filter_even(numbers):
#     for number in numbers:
#         if number % 2 == 0:
#             yield number


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# result = filter_even(my_list)

# for value in result:
#     print(value)

# -------------------------------
# Task 6.
# -------------------------------

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_gen = (x for x in my_list if x % 2 == 0)

# for number in even_gen:
#     print(number)


# -------------------------------
# Task 7.
# -------------------------------

def read_file_lines(file_path):
    with open(file_path, encoding='utf-8') as file:
        for line in file:
            yield line