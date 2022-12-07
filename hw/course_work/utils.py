import random

def load_random_word(data, used_class):

    random_word_index = random.randint(0, len(data)-1)
    random_word = data[random_word_index]

    random_word = used_class(random_word['word'], random_word['subwords'])

    return random_word







