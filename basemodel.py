# Code by Anand A Nair
#
# Enter your word guess and the game's output in command line after running the program
# The game's output will be 5 spaced integers depicting output for each charcter cell in order
#
# 1 - correct position and character
# 2 - correct character, wrong position
# 0 - wrong character
#
# eg: 2 0 2 0 1
#  
# Use any word from output list in each iteration as next guess
# 
#

import sys
import re
import string
import json

# Creation of Word Lists that will be used while running the program
words_list = list()
words_list_iter = list()
words_to_be_removed = list()

# Master Word List Data File
words_file = open('data/filtered_words.txt', 'r')

for line in words_file:
    word = line.strip()
    words_list.append(word)

words_file.close()

possibilities = list() # possibilities indicate what character can go in each position

for i in range(5):
    possibilities.append([char for char in string.ascii_uppercase])

words_dist_file = open('data/word_dist.json', 'r')

words_dist_dict = json.load(words_dist_file)

words_dist_file.close()

correct_chars = list()

for i in range(6):
    words_list_iter = []
    words_to_be_removed = []
    word_input = input("Enter your word guess: ")
    word_chars = list()
    word_chars[:0] = word_input
    info = list(map(int, input("Enter the game's output: ").split()))

    for i in range(5):
        if info[i] == 0:
            for possibility in possibilities:
                if word_chars[i] in possibility:
                    possibility.remove(word_chars[i]) # removing from all positions given charcter is not present in word
        elif info[i] == 1:
            if word_chars[i] not in correct_chars:
                correct_chars.append(word_chars[i])
            possibilities[i] = [word_chars[i]] # if correct position and character, changing the possibility to only allow that character
        elif info[i] == 2:
            if word_chars[i] not in correct_chars:
                correct_chars.append(word_chars[i])
            if word_chars[i] in possibilities[i]:
                possibilities[i].remove(word_chars[i]) # removing correct character from wrong position
    """ 
    words_list_iter = []
    wrong_chars_curr = list()
    correct_chars_curr = list()
    correct_chars_curr_wrong_pos = list()
    word_input = input()
    word_chars = list()
    word_chars[:0] = word_input
    info = list(map(int, input().split()))

    for i in range(5):
        if info[i] == 0:
            wrong_chars_curr.append(word_chars[i])
            for possibility in possibilities:
                if word_chars[i] in possibility:
                    possibility.remove(word_chars[i])
        elif info[i] == 1:
            correct_chars_curr.append(word_chars[i])
            possibilities[i] = [word_chars[i]]
        elif info[i] == 2:
            correct_chars_curr.append(word_chars[i])
            if word_chars[i] in possibilities[i]:
                possibilities[i].remove(word_chars[i])
    """

    # regex creation - need to modify once more is learnt about the concept

    regex_string = '[' + ''.join(possibilities[0]) + ']' + '[' + ''.join(possibilities[1]) + ']' + \
        '[' + ''.join(possibilities[2]) + ']' + '[' + ''.join(possibilities[3]) + ']' + \
            '[' + ''.join(possibilities[4]) + ']'
    
    # print(regex_string) # debug line
    
    # regex = re.compile(regex_string) # unwanted line

    # shortlisting based on regular expression
    for word in words_list: # analyse logically whether words_list_iter can be used instead of whole words_list
        if re.match(regex_string, word): 
            words_list_iter.append(word)

    # print(len(words_list_iter)) # debug line

    for word in words_list_iter:
        if not all(char in word for char in correct_chars): # shortlisting words to remove not containing required characters
            words_to_be_removed.append(word)
    
    #print(len(words_to_be_removed))
    
    #print(words_to_be_removed)

    words_list_iter = [word for word in words_list_iter if word not in words_to_be_removed] # removing words without required characters

    #print(len(words_list_iter))

    print(words_list_iter)
    #print(possibilities)

'''

words_file.close()

wrong_chars = list()
correct_chars = list()

for i in range(6):
    new_words_list = list()
    wrong_chars_curr = list()
    correct_chars_curr = list()
    word_input = input()
    word_chars = list()
    word_chars[:0] = word_input
    info = list(map(int, input().split()))

    for i in range(5):
        if info[i] == 0:
            wrong_chars_curr.append(word_chars[i])
        elif info[i] == 1:
            correct_chars_curr.append(word_chars[i])
        elif info[i] == 2:
            correct_chars_curr.append(word_chars[i])

    for word in words_list:
        for char in wrong_chars_curr:
            if char in word:
                new_words_list.append(word)

        
        for char in correct_chars_curr:
            if char not in word:
                new_words_list.append(word)

    words_list = [word for word in words_list if word not in new_words_list]

    print(words_list)

    '''