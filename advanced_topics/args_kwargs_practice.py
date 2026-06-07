# --------------------------------
# Task 1
# --------------------------------

# def find_highest_score(*args):
#     return max(*args)


# print(f'[Analytics] Maximum score for the exam: {find_highest_score(85, 92, 78, 99, 64)}')


# --------------------------------
# Task 2
# --------------------------------

def print_user_profile(**kwargs):
    for key, value in kwargs.items():
        print(f'-{key}: {value}')


print_user_profile(username="alex_dev", age=30, email="alex@example.com")