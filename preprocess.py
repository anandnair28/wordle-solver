import json
import string

from numpy import character

freq_dict = dict()
word_dist_dict = dict()

for char in string.ascii_uppercase:
    freq_dict[char] = 0
    word_dist_dict[char] = list()

words_file = open('data/filtered_words.txt', 'r')

for line in words_file:
    word = line.strip()
    chars = set(word)
    for char in chars:

        freq_dict[char] += 1
        word_dist_dict[char].append(word)
        
        '''
        freq_dict[char] = freq_dict.get(char, 0) + 1
        
        if char not in word_dist_dict:
            word_dist_dict[char] = [word]
        else:
            word_dist_dict[char].append(word)
        '''

words_file.close()
            
word_dist_file = open('data/word_dist.json', 'w')
json.dump(word_dist_dict, word_dist_file)
word_dist_file.close()

freq_file = open('data/frequencies.json', 'w')
json.dump(freq_dict, freq_file)
freq_file.close()

words_file.close()