# --------------------------------
# Task 1
# --------------------------------

# def find_highest_score(*args):
#     return max(*args)


# print(f'[Analytics] Maximum score for the exam: {find_highest_score(85, 92, 78, 99, 64)}')


# --------------------------------
# Task 2
# --------------------------------

# def print_user_profile(**kwargs):
#     for key, value in kwargs.items():
#         print(f'- {key}: {value}')


# print_user_profile(username="alex_dev", age=30, email="alex@example.com")

# --------------------------------
# Task 3
# --------------------------------

def analyze_metrics(*args, **kwargs):
    for key, value in kwargs.items():
        print(f'- {key}: {value}')
    print(f'[Analytics] Average metric value: {sum(args)/len(args)}')


analyze_metrics(120, 150, 180, department="IT", manager="Alexey")