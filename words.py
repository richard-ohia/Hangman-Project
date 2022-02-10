"""
Bismallah
"""
import random

def get_word_list(choice):
    words = []
    with open(choice) as word_file:
        for line in word_file:
            if (len(line) >= 4):
                words.append(line.strip())
    return words

def game_word(choice):
    word_list = get_word_list(choice)
    rand = random.randrange(len(word_list))
    return word_list[rand].upper()