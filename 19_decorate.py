"""Декоратор uppercase_elements
Ваша задача написать логику работы декоратора uppercase_elements, который умеет работать с функциями, возвращающими коллекции элементов. Задача декоратора uppercase_elements преобразовать каждый строковый элемент коллекции к заглавному регистру. В случае, если оригинальная функция возвращает словарь, то элементом считаем только строковые ключи словаря.

Элементы, не являющиеся строкой, не должны изменяться декоратором uppercase_elements

Гарантируется, что коллекции, возвращаемые оригинальной функцией, не являются вложенными"""

# def uppercase_elements(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#
#         if isinstance(result, dict):
#             return {k.upper() if isinstance(k, str) else k: v for k, v in result.items()}
#
#         elif isinstance(result, list):
#             return [item.upper() if isinstance(item, str) else item for item in result]
#
#         elif isinstance(result, set):
#             return {item.upper() if isinstance(item, str) else item for item in result}
#
#         elif isinstance(result, tuple):
#             return tuple(item.upper() if isinstance(item, str) else item for item in result)
#         else:
#             return result
#
#     return wrapper
#
#
# @uppercase_elements
# def my_func(name, surname):
#     return ['temple', 'store', name, surname, *[1, 2, 3]]
#
# print(my_func('Gerard', 'Pique'))


# def dec(fn):
#     print("Запуск декоратора")
#
#     def wrapper(*args, **kwargs):
#         print("Запуск inner")
#         return fn(*args, **kwargs)
#
#     return wrapper
#
# @dec
# def say_hello():
#     return 'Hello'
# #
# # print(say_hello())
# # print(say_hello())
# # print(say_hello())


'''
Декоратор limit_query
Напишите декоратор limit_query, который ограничивает вызов оригинальной функции так, чтобы она могла вызываться не 
больше трех раз. Когда декорируемая функция исчерпает лимит вызовов, необходимо выводить на экран фразу

 «Лимит вызовов закончен, все 3 попытки израсходованы»

Если лимит исчерпан, оригинальная функция не должна быть вызвана, декоратор возвращает None
'''


# def limit_query(func):
#     count = 0
#     def inner(a: int, b: int):
#         nonlocal count
#         if count < 3:
#             count += 1
#             return func(a, b)
#         print(f'Лимит вызовов закончен, все 3 попытки израсходованы')
#         return
#     inner.__name__ = func.__name__
#     return inner
#
#
# @limit_query
# def add(a: int, b: int):
#     return a + b
#
# print(add(4, 5))
# print(add(5, 8))
# print(add(9, 43))
# print(add(10, 33))
# print(add.__name__)


"""
Декоратор no_side_effects_decorator
Напишите декоратор no_side_effects_decorator, который защищает от побочных действий функций

Sample Input 1:

@no_side_effects_decorator
def add_element(data, element):
    data.append(element)
    return data


my_list = [1, 2, 3]
print('Результат вызова =', add_element(my_list, 4))
print('Результат вызова =', add_element(my_list, 5))
print(my_list)
print(add_element.__name__)


Sample Output 1:

Результат вызова = [1, 2, 3, 4]
Результат вызова = [1, 2, 3, 5]
[1, 2, 3]
add_element
"""


# from functools import wraps
#
#
# def no_side_effects_decorator(func):
#
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(func.__annotations__)
#         return func(*args, **kwargs)
#
#     print(func.__annotations__)
#     return wrapper
#
#
#
# @no_side_effects_decorator
# def add_element(data, element):
#     data.append(element)
#     return data
#
# my_list = [1, 2, 3]
# print('Результат вызова =', add_element(my_list, 4))
# print('Результат вызова =', add_element(my_list, 5))
# print(my_list)
# print(add_element.__name__)

"""
Валидация args
Напишите декоратор validate_all_args_str, который проверяет на корректность (валидирует) переданные позиционные аргументы. Корректным он считает любое строковое значение, стоящее в позиционном аргументе; ключевые аргументы при проверке игнорируются. Если было передано хотя бы одно не строковое значение в позиционный аргумент, функция-декоратор validate_all_args_str должна

вывести на экран фразу «Все аргументы должны быть строками»
вернуть None и не запускать оригинальную  функцию
Если же все аргументы корректны, validate_all_args_str запускает оригинальную функцию со всеми переданными значениями.

 

 
Sample Input 1:

@validate_all_args_str
def concatenate(*args):
    result = ""
    for arg in args:
        result += arg
    return result


print(concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"))
Sample Output 1:

НуКогдаУжеЯВыучуПитон?
"""

# def validate_all_args_str(func):
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             if not isinstance(arg, str):
#                 print('Все аргументы должны быть строками')
#                 return
#         return func(*args, **kwargs)
#     return wrapper
#
#
# def validate_all_kwargs_int_pos(func):
#     def wrapper(*args, **kwargs):
#         for value in kwargs.values():
#             if not type(value) == int or value <= 0:
#                 print('Все именованные аргументы должны быть положительными числами')
#                 return
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @validate_all_args_str
# @validate_all_kwargs_int_pos
# def concatenate(*args, **kwargs):
#     result = ""
#     for arg in args + tuple(kwargs.values()):
#         result += str(arg)
#     return result
#
# print(concatenate('Hello', 'World', a='sdf', b=2, c=2))



"""
Фильтрация аргументов
Ваша задача создать два декоратора

    1️⃣ filter_even, который фильтрует только позиционные аргументы. Среди всех переданных значений он оставляет только четные числа, False и коллекции, длина которых четная

    2️⃣ delete_short, который фильтрует только именованные аргументы. Среди всех переданных значений он оставляет только те, имена которых более четырех символов

Sample Input 1:

@delete_short
def info_kwargs(**kwargs):
    '''Выводит информацию о переданных kwargs'''
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')

info_kwargs(first_name="John", last_name="Doe", age=33)
Sample Output 1:

first_name = John
last_name = Doe

"""

# def filter_even(func):
#     def wrapper(*args, **kwargs):
#         result_list: list = []
#         for x in args:
#             if ((type(x) == int and x % 2 == 0)
#                     or (hasattr(x, '__iter__') and len(x) % 2 == 0)
#                     or x == False):
#                 result_list.append(x)
#         return func(*result_list, **kwargs)
#     return wrapper
#
#
# def delete_short(func):
#     def wrapper(*args, **kwargs):
#         result_dict : dict = {}
#         for key, value in kwargs.items():
#             if len(key) > 4:
#                 result_dict [key] = value
#         return func(*args, **result_dict )
#     return wrapper
#
# @filter_even
# def concatenate(*args):
#     result = ""
#     for arg in args:
#         result += arg
#     return result
#
# print(concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"))
#
# @filter_even
# @delete_short
# def concatenate(*args, **kwargs):
#     result = ""
#     for arg in args + tuple(kwargs.values()):
#         result += str(arg)
#     return result
#
#
# print(concatenate("Я", "хочу", "Выучить", "Питон", a="За", qwerty=10, c="Месяцев"))

""" 
универсальный способ проверки

from collections.abc import Collection

#и далее проверка
isinstance(arg, Collection)

есть еще такой вариант: hasattr(i, "__iter__"), без подключения модулей 
"""

"""
"""