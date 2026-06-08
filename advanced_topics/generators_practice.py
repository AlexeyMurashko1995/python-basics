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

def custom_range(n):
    for number in range(1, n + 1):
        yield number


result = custom_range(5)

for value in result:
    print(value)