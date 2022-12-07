import random
import requests
import json
import utils
from basicword import BasicWord
from player import Player

r = requests.get("https://www.jsonkeeper.com/b/VZ7S") #берем данные с сайта и сохраняем в json формате
data = r.json()


user = input(f'Введите имя: ')

'''Сохраняет имя пользователя и
создает экземпляр объекта с названием в
виде имени пользователя'''

user = Player(user)

print(f"Хай!")

''' функция создает экземпляр класса BasicWord'''

question = utils.load_random_word(data, BasicWord)

print(question.make_question())


while user.get_lenth_used_words() < question.get_length_subwords():
    user_attemp = input("Введите слово: ")

    """основной цикл, который остановится при угадывании всех слов либо
при вводе stop"""

    if question.answer_check(user_attemp):
        if user.if_word_used(user_attemp):
            print(f"Ответ принят!")
            user.save_used_words(user_attemp)

    elif user_attemp == 'stop':
        break

    else:
        print(f"Ответ не подходит")

"""Выдает статистику"""
print(f" Игра завершена, вы угадали {user.get_lenth_used_words()} слов!")












