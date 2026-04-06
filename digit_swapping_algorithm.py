def count_numbers(a):
    count = 0
    while a > 0:
        a //= 10
        count += 1
    return count


def change_number(a):
    num_count = count_numbers(a)
    first_digit = a // (10 ** (num_count - 1))
    last_digit = a % 10
    between_digits = (a % (10 ** (num_count - 1))) // 10
    final_number = (last_digit * (10 ** (num_count - 1))) + (between_digits * 10) + first_digit
    return final_numbe


def get_sum_of_numbers(a,b):
    return a + b


def main():
    first_number = int(input('Enter the first number: '))
    second_number = int(input('Enter the second number: '))
    status_first = count_numbers(first_number)
    status_second = count_numbers(second_number)

    if status_first < 3:
        print('Invalid input. The first number must have at least 3 digits')
    elif status_second < 4:
        print('Invalid input. The second number must have at least 4 digits.')
    else:
        print(f'The first number has {status_first} digits')
        print(f'The second number has {status_second} digits')

        changed_first_number = change_number(first_number)
        print(f'Changed first number: {changed_first_number}')

        changed_second_number = change_number(second_number)
        print(f'Changed second number: {changed_second_number}')

        print(f'Sum of changed numbers: {get_sum_of_numbers(changed_first_number, changed_second_number)}')


main()

print('*' * 30)
