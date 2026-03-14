# A program to find the length of the longest word in a sentence
sentence = input('Enter a sentence: ')

max_length = 0
current_word_len = 0

for char in sentence:
    if char != ' ':
        current_word_len += 1
    else:
        # Check the record when a space is encountered
        if current_word_len > max_length:
            max_length = current_word_len
        # Always reset the counter for the next word
        current_word_len = 0

# Final check for the last word (since sentences don't always end with a space)
if current_word_len > max_length:
    max_length = current_word_len

print(f"The length of the longest word is: {max_length}")