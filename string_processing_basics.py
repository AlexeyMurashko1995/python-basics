# TASK 1: THE SPICE COUNTER (Frequency Analysis)
# Counting specific characters in a string to analyze data distribution.
phrase = input('Enter the phrase: ').lower()
s_count = 0
p_count = 0

for char in phrase: 
    if char == 's':
        s_count += 1
    elif char == 'p':
        p_count += 1

print(f'Letter "s" appears: {s_count} times')
print(f'Letter "p" appears: {p_count} times')
print('-' * 25)


# TASK 2: THE SANDWICH METHOD (Decryption Algorithm)
# Restoring a word by splitting it based on even/odd positions.
word = input('Enter the encrypted word: ')
left_side = ''
right_side = ''

for index, char in enumerate(word, start=1):
    if index % 2 != 0:
        left_side = left_side + char  # Normal order for odd indices
    else:
        right_side = char + right_side # Reversed order for even indices

result = left_side + right_side
print(f'Decrypted message: {result}')
print('-' * 25)


# TASK 3: DATA PURIFICATION (Character Filtering)
# Removing "noise" from data like $, %, and #.
raw_data = input('Enter phrase to clean ($%#): ')
clean_text = ''
for char in raw_data:
    if (char != '$') and (char != '%') and (char != '#'):
        clean_text = clean_text + char

print(f'Cleaned output: {clean_text}')
print('-' * 25)

# TASK 4. IDENTITY MATRIX GENERATOR (AI Foundation)
# Outputting '1' only when row index equals column index.
number = int(input('Enter the number: '))
for col in range(number):
    for row in range(number):
        if row == col:
            print('1', end='\t')
        else:
            print('0', end='\t')
    print()
