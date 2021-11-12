"""
Bismallah
"""
import random

def get_word_list():
    words = []
    with open("words.txt") as word_file:
        for line in word_file:
            if (len(line) > 4):
                words.append(line.strip())
    return words

def game_word():
    word_list = get_word_list()
    rand = random.randrange(len(word_list) + 1)
    return word_list[rand].upper()