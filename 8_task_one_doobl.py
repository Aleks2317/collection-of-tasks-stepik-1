'''Находим первый дубль
Напишите функцию get_first_repeated_word, которая имеет один параметр words - список, состоящий из нескольких слов.
Функция должна найти первый элемент, который образует дубль с ранее стоящими элементами,
и вернуть его в качестве результата. Если передан список, в котором все слова различны,
функция get_first_repeated_word должна вернуть None
Регистр букв при сравнении нужно учитывать

Для функции  get_first_repeated_word  дополнительно нужно добавить

 1️⃣  док-строку  Находит первый дубль в списке

 2️⃣  аннотации при помощи модуля typing
 '''
from typing import List, Optional


def get_first_repeated_word(words: List[str]) -> Optional[str]:
    '''Находит первый дубль в списке'''
    if len(set(words)) == len(words):
        return
    for word in range(1, len(words)):
        if words[ : word + 1].count(words[word]) > 1:
            return words[word]

print(get_first_repeated_word.__doc__)
print(get_first_repeated_word.__annotations__)
print(get_first_repeated_word(['hello', 'hi', 'hello']))
print(get_first_repeated_word(['ab', 'ca', 'bc', 'Ab', 'cA', 'aB', 'bc']))
print(get_first_repeated_word(['ab', 'ca', 'bc', 'ca', 'ab', 'bc']))

from typing import List, Optional

def get_first_repeated_word(words: List[str]) -> Optional[str]:
    '''Находит первый дубль в списке'''
    st = set()
    for el in words:
        if el in st: return el
        st.add(el)
    return None


