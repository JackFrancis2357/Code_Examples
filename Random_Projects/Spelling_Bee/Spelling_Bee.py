import pandas as pd
import numpy as np
import pygame
from gtts import gTTS

pygame.mixer.init()

g5e = pd.read_excel('Word_List_Updated.xlsx', sheet_name='Sheet2', dtype=str).values
g5a = pd.read_excel('Word_List_Updated.xlsx', sheet_name='Sheet3', dtype=str).values
g5d = pd.read_excel('Word_List_Updated.xlsx', sheet_name='Sheet4', dtype=str).values
g6e = pd.read_excel('Word_List_Updated.xlsx', sheet_name='Sheet5', dtype=str).values
g6a = pd.read_excel('Word_List_Updated.xlsx', sheet_name='Sheet6', dtype=str).values
g6d = pd.read_excel('Word_List_Updated.xlsx', sheet_name='Sheet7', dtype=str).values
g7e = pd.read_excel('Word_List_Updated.xlsx', sheet_name='Sheet8', dtype=str).values
g7a = pd.read_excel('Word_List_Updated.xlsx', sheet_name='Sheet9', dtype=str).values
g7d = pd.read_excel('Word_List_Updated.xlsx', sheet_name='Sheet10', dtype=str).values
g8e = pd.read_excel('Word_List_Updated.xlsx', sheet_name='Sheet11', dtype=str).values
g8a = pd.read_excel('Word_List_Updated.xlsx', sheet_name='Sheet12', dtype=str).values
g8d = pd.read_excel('Word_List_Updated.xlsx', sheet_name='Sheet13', dtype=str).values


def remove_nan_concat(d1, d2, d3):
    d_list = [d1, d2, d3]
    d_list = [d.ravel() for d in d_list]
    d_list = [np.delete(d, np.where(d == ['nan']), axis=0) for d in d_list]
    return np.concatenate((d_list[0], d_list[1], d_list[2]))


def practice_spelling():
    ans = input('What grade level would you like to practice? If you would like all words type all: ')
    if ans == '5':
        g5 = remove_nan_concat(g5e, g5a, g5d)
        return g5
    elif ans == '6':
        g6 = remove_nan_concat(g6e, g6a, g6d)
        return g6
    elif ans == '7':
        g7 = remove_nan_concat(g7e, g7a, g7d)
        return g7
    elif ans == '8':
        g8 = remove_nan_concat(g8e, g8a, g8d)
        return g8
    elif ans.upper() == 'ALL':
        g5 = remove_nan_concat(g5e, g5a, g5d)
        g6 = remove_nan_concat(g6e, g6a, g6d)
        g7 = remove_nan_concat(g7e, g7a, g7d)
        g8 = remove_nan_concat(g8e, g8a, g8d)
        all_words = np.concatenate((g5, g6, g7, g8))
        return all_words
    else:
        print('That''s not a valid answer. Acceptable answers are 5, 6, 7, 8, or all')
        print('\n')
        return False


def get_random_word(wl):
    if len(wl) == 0:
        return 0, 0
    word = wl[np.random.randint(0, len(wl))]
    wl = np.delete(wl, np.where(wl == word), axis=0)
    tts = gTTS(text=word, lang='en')
    filename = '/tmp/temp.mp3'
    tts.save(filename)
    pygame.mixer.music.load('/tmp/temp.mp3')
    pygame.mixer.music.play()
    return word, wl


word_list = practice_spelling()
while word_list is False:
    word_list = practice_spelling()

new_word, practicing = True, True
total_words, correct_words = 0, 0
words_missed = []
print('If you would like to repeat, please type repeat. If you would like to quit, please type exit')
while practicing:
    if new_word is True:
        word, word_list = get_random_word(word_list)
        if word == 0 and word_list == 0:
            print('You have finished all of the words for this section.')
            total_words += 1
            break
        total_words += 1
    ans = input('Please spell the word: ')
    if ans.upper() == word.upper():
        print('Correct!')
        new_word = True
        correct_words += 1
    elif ans.upper() == 'EXIT':
        practicing = False
    elif ans.upper() == 'REPEAT':
        pygame.mixer.music.play()
        new_word = False
    else:
        print('Incorrect. The correct spelling is %s' % word)
        new_word = True
        words_missed.append(word)

print('Great job practicing!')
print('You got %s correct out of %s total words' % (correct_words, total_words - 1))
print('The words you got incorrect were: %s' % words_missed)
