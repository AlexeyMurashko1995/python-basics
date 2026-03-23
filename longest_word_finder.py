phrase = input('Enter the phrase: ')
summ = ''
#print('\nFiltered text:', end = ' ')
for char in phrase: 
    if char == '$':
        summ = char + summ
    else:
        print(char, end = ' ')