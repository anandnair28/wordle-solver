import re

n_char = 5

input_file = open('data/words_alpha.txt', 'r')
output_file = open('data/filtered_words.txt', 'w')

for line in input_file:
    word = line.strip()
    if not word.isalpha():
        continue
    if len(word) == 5:
        word = word.upper()
        output_file.write(word + '\n')

input_file.close()
output_file.close()