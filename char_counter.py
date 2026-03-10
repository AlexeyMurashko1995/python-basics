text = input('Enter the text: ')
first_letter_to_find = input('Enter the first character to find: ').lower()
second_letter_to_find = input('Enter the second character to find: ').lower()
first_count = 0
second_count = 0

for char in text:
    if char.lower() == first_letter_to_find:
        first_count += 1
    elif char.lower() == second_letter_to_find:
        second_count += 1

print(f'Character "{first_letter_to_find}" appears {first_count} times.')
print(f'Character "{second_letter_to_find}" appears {second_count} times.')