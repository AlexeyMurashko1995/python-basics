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

# def analyze_metrics(*args, **kwargs):
#     for key, value in kwargs.items():
#         print(f'- {key}: {value}')
#     print(f'[Analytics] Average metric value: {sum(args)/len(args)}')


# analyze_metrics(120, 150, 180, department='IT', manager='Alexey')

# --------------------------------
# Task 4
# --------------------------------

# def merge_strings(*args, uppercase=False):
#     result = ' '.join(args)
#     if uppercase:
#         result = result.upper()
#     return result


# text1 = merge_strings("hello", "world", uppercase=False)
# text2 = merge_strings("python", "interview", "prep", uppercase=True)

# print(text1)
# print(text2)

# --------------------------------
# Task 5
# --------------------------------

def configure_settings(defaults, **custom):
    new_defaults = defaults.copy()
    new_defaults.update(custom)
    return new_defaults


default_config = {'theme': 'light', 'language': 'en', 'notifications': True}

final_config = configure_settings(default_config, theme='dark', language='pl')

print(default_config)
print(final_config)