# The following is from basemodel.py

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