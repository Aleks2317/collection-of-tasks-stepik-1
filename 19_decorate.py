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

# import copy
# from functools import wraps
#
# def no_side_effects_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         # Создаем глубокие копии аргументов
#         args_copy = copy.deepcopy(args)
#         kwargs_copy = copy.deepcopy(kwargs)
#         # Вызываем оригинальную функцию с копиями аргументов
#         result = func(*args_copy, **kwargs_copy)
#         # Возвращаем глубокую копию результата
#         return copy.deepcopy(result)
#     return wrapper


"""
Декоратор add_args
Напишите декоратор add_args, который добавляет к переданным аргументам еще два значения: 
строку «begin» в начало аргументов, строку «end» в конец. 
Также декоратор должен сохранить первоначальное имя декорируемой функции и ее строку документации
"""

# from functools import wraps
#
# def add_args(func):
#     @wraps(func)
#     def wrapper(*args):
#         args = ('begin', ) + args + ('end',)
#         return func(*args)
#     return wrapper
#
#
# @add_args
# def concatenate(*args):
#     """
#     Возвращает конкатенацию переданных строк
#     """
#     return ', '.join(args)
#
#
# print(concatenate('hello', 'world', 'my', 'name is', 'Artem'))
# print(concatenate('my', 'name is', 'Artem'))
# print(concatenate.__name__)
# print(concatenate.__doc__.strip())
#
#
# @add_args
# def find_max_word(*args):
#     """
#     Возвращает слово максимальной длины
#     """
#     return max(args, key=len)
#
# print(find_max_word('my'))
# print(find_max_word('my', 'how'))
# print(find_max_word('my', 'how', 'maximum'))
# print(find_max_word.__name__)
# print(find_max_word.__doc__.strip())

"""
  Декоратор explicit_args
Реализуйте декоратор explicit_args, который не позволяет запускать оригинальную функцию, если были переданы позиционные аргументы. Декоратор explicit_args должен выводить фразу 

Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений
и предотвращать запуск оригинальной функции

Sample Input 1:

@explicit_args
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b

print(add(10, 20))
Sample Output 1:

Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений
None
Sample Input 2:

@explicit_args
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b

print(add(a=10, b=20))
Sample Output 2:

30
"""
# from functools import wraps
#
#
# def explicit_args(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         if args:
#             print('Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений')
#             return
#         return func(**kwargs)
#
#     return inner
#
# @explicit_args
# def add(a: int, b: int) -> int:
#     '''Возвращает сумму двух чисел'''
#     return a + b
#
# print(add(10, 20))
#
# @explicit_args
# def add(a: int, b: int) -> int:
#     '''Возвращает сумму двух чисел'''
#     return a + b
#
# print(add(a=10, b=20))

"""
Декоратор reverse
Реализуйте декоратор reverse, который сделает так, чтобы декорированная функция принимала все свои позиционные аргументы в обратном порядке. Именованные аргументы должны игнорироваться декоратором reverse.

Также нужно сохранить информацию о декорируемой функции.

Sample Input 1:

@reverse
def get_max_index(*args):
    if not args:
        return None
    max_index = 0
    for i in range(len(args)):
        if args[i] > args[max_index]:
            max_index = i
    return max_index
    
    
print(get_max_index(1, 2, 3, 4, 5))
print(get_max_index(3, 4, 1, 5, 2))
print(get_max_index(5, 3, 4, 1, 2))
print(get_max_index.__name__)
Sample Output 1:

0
1
4
get_max_index
Sample Input 2:

def get_average(*args, **kwargs):
    summa = sum(args) + sum(kwargs.values())
    count = len(args) + len(kwargs)
    return summa/count
    
print(get_average(1, 2, 3, 4, 5, a=10, b=15, c=12))
# декорируем
get_average = reverse(get_average)
print(get_average(1, 2, 3, 4, 5, a=10, b=15, c=12))
Sample Output 2:

6.5
3.0
Напишите программу. Тестируется через stdin → stdout
"""

# from functools import wraps
#
#
# def reverse(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         args = reversed(args)
#         return func(*args)
#     return wrapper
#
#
# def get_average(*args, **kwargs):
#     summa = sum(args) + sum(kwargs.values())
#     count = len(args) + len(kwargs)
#     return summa / count
#
#
# print(get_average(1, 2, 3, 4, 5, a=10, b=15, c=12))
# # декорируем
# get_average = reverse(get_average)
# print(get_average(1, 2, 3, 4, 5, a=10, b=15, c=12))


'''Декоратор monkey_patching
Monkey patch -  это прием в программировании, который используется для динамического изменения поведения фрагмента кода во время выполнения.

Ваша задача написать декоратор monkey_patching, который заменяет значения всех переданных аргументов при вызове оригинальной функции следующим образом:

    ➕   значение каждого позиционного аргумента заменяется на строку «Monkey»

    ➕   значение каждого именованного аргумента заменяется на строку «patching»'''

# from functools import wraps
#
#
# def monkey_patching(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         new_args = ['Monkey' for _ in range(len(args))]
#         new_kwargs = {key: 'patching' for key in kwargs.keys()}
#         return func(*new_args, **new_kwargs)
#     return wrapper
#
#
# @monkey_patching
# def print_args_kwargs(*args, **kwargs):
#     for i, value in enumerate(args):
#         print(i, value)
#     for k, v in sorted(kwargs.items()):
#         print(f'{k} = {v}')
#
#
# print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)


# from functools import wraps
#
#
# def counting_calls(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.call_count += 1
#         return func(*args, **kwargs)
#     wrapper.call_count = 0
#     return wrapper
#
#
#
# @counting_calls
# def add(a: int, b: int) -> int:
#     '''Возвращает сумму двух чисел'''
#     return a + b
#
#
# print(add.__name__)
# print(add.__doc__)
#
# print(add(10, b=20))
# print(add.__annotations__)
# print(add.call_count)
# print(add(30, 5))
# print(add.call_count)
# print(add.__getattribute__())



"""
Декоратор check_count_args
Напишите декоратор check_count_args, который проверяет количество переданных аргументов. Проверка заключается в следующем

в оригинальную функцию должно быть передано только два аргумента и неважно позиционно или по ключу. Если это условие выполняется, возвращаем результат вызова оригинальной функции
 
Если передано меньшее количество, декоратор должен вывести строку «Not enough arguments» и не должен запускать оригинальную функцию;
 
Если передано более двух аргументов, то декоратор должен вывести строку «Too many arguments» и не должен запускать оригинальную функцию.
Не забывайте сохранять имя функции и строку документации. Для решения необходимо написать только реализацию декоратора check_count_args

Sample Input 1:

@check_count_args
def add_numbers(x, y):
    '''Return sum of x and y'''
    return x + y


print(add_numbers(4, 5))
print(add_numbers.__name__)
print(add_numbers.__doc__.strip())
Sample Output 1:

9
add_numbers
Return sum of x and y
"""

# from functools import wraps
#
#
# def check_count_args(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         count_args = len(args) + len(kwargs)
#         if count_args == 2:
#             return func(*args, **kwargs)
#         print('Not enough arguments' if count_args < 2 else 'Too many arguments')
#
#     return wrapper
#
#
# @check_count_args
# def add_numbers(x, y):
#     """Return sum of x and y"""
#     return x + y
#
# add_numbers(3, 5, 6)


# from functools import wraps
#
#
# def cache_result(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         args_ = tuple(args) + tuple(kwargs.items())
#         if args_ in wrapper.cache_:
#             print(f'[FROM CACHE] Вызов {wrapper.__name__} = {wrapper.cache_[args_]}')
#             return wrapper.cache_.get(args_)
#
#         wrapper.cache_[args_] = func(*args, **kwargs)
#         return func(*args, **kwargs)
#
#     wrapper.cache_ = dict()
#     return wrapper
#
#
# @cache_result
# def add(a, b):
#     return a + b
#
# print(add(4, 4)) # 1й раз с такими атрибутами
# print(add(4, 5)) # 1й раз с такими атрибутами
# print(add(4, 6)) # 1й раз с такими атрибутами
# print(add(4, 5)) # достаем из кеша
# print(add(5, 4)) # 1й раз с такими атрибутами
# print(add(6, 3)) # 1й раз с такими атрибутами
# print(add(a=6, b=3)) # 1 раз с такими атрибутами: позицицинные!=именованные
# print(add(a=6, b=3)) # достаем из кеша


"""
Декоратор counting_calls - 2
Усовершенствуем ранее созданный декоратор counting_calls, добавив отслеживание переданных аргументов при каждом вызове. 

Для этого декоратор counting_calls должен добавить в декорируемой функции атрибут calls - список, в который будут сохраняться все переданные аргументы в момент вызова в виде словаря. Каждый словарь должен иметь два ключа: args и kwargs для сохранения соответствующих аргументов.

Sample Input 1:

@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b


print(add.__name__)
print(add.__doc__)

print(add(10, b=20))
print('Количество вызовов =', add.call_count)
print(add.calls)

print(add(5, 6))
print(add.calls[1])
"""

# from functools import wraps
#
#
# def counting_calls(f):
#     @wraps(f)
#     def wrapper(*args, **kwargs):
#         wrapper.calls.append({'args': args, 'kwargs': kwargs})
#         wrapper.call_count = len(wrapper.calls)
#         return f(*args, **kwargs)
#     wrapper.calls = []
#     wrapper.call_count = 0
#     return wrapper
#
#
# @counting_calls
# def add(a: int, b: int) -> int:
#     '''Возвращает сумму двух чисел'''
#     return a + b
#
# print(add(10, b=20))
# print(add(7, 5))
# print(add(12, 45))
# print('Количество вызовов =', add.call_count)
# print(add.calls[2])
#
# print(add(b=11, a=22))
# print(add.calls[3])

# def my_func(x):
#     return 15
#
#
# a = [1, 2, 3, 4, 5]
# print(list(filter(my_func, a)))

""" Декораторы с параметрами"""

"""Декоратор multiply_result_by
Создайте декоратор multiply_result_by, который принимает аргумент N и возвращает функцию-декоратор, которая умножает результат декорированной функции на N
"""
# from functools import wraps
#
# def multiply_result_by(n):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs) * n
#         return wrapper
#     return decorator
#
#
# @multiply_result_by(2)
# def my_function(x, y):
#     return x + y
#
#
# print(my_function(5, 6))


# from functools import wraps
#
#
# def limit_query(limit):
#     def decorated(func):
#         count = limit
#         @wraps(func)
#         def inner(a: int, b: int):
#             nonlocal count
#             if count > 0:
#                 count -= 1
#                 return func(a, b)
#             print(f'Лимит вызовов закончен, все {limit} попытки израсходованы')
#             return
#         return inner
#     return decorated
#
#
# @limit_query(3)
# def add(a: int, b: int):
#     return a + b
#
# print(add(4, 5))
# print(add(5, 8))
# print(add(9, 43))
# print(add(10, 33))
# print(add.__name__)


"""
Декоратор monkey_patching - 2
Ваша задача переписать декоратор monkey_patching. Ранее он заменял значения всех переданных аргументов при вызове оригинальной функции следующим образом:

    ➕   значение каждого позиционного аргумента заменяется на строку «Monkey»

    ➕   значение каждого именованного аргумента заменяется на строку «patching»

Теперь необходимо завести параметры arg и kwarg, при помощи которых можно влиять на значения, которые будут проставляться в позиционные и именованные аргументы. Параметры arg и kwarg являются необязательными для передачи, их значения по умолчанию «Monkey» и «patching» соответственно.

Sample Input 1:

@monkey_patching(arg='Super')
def print_args_kwargs(*args, **kwargs):
    for i, value in enumerate(args):
        print(i, value)
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')


print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)
Sample Output 1:

0 Super
1 Super
2 Super
3 Super
a = patching
b = patching
t = patching
w = patching
"""


# from functools import wraps
#
#
# def monkey_patching(arg= 'Monkey', kwarg= 'patching'):
#     def decorated(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             new_args = [arg for _ in range(len(args))]
#             new_kwargs = {key: kwarg for key in kwargs.keys()}
#             return func(*new_args, **new_kwargs)
#         return wrapper
#     return decorated
#
# @monkey_patching(arg='Super')
# def print_args_kwargs(*args, **kwargs):
#     for i, value in enumerate(args):
#         print(i, value)
#     for k, v in sorted(kwargs.items()):
#         print(f'{k} = {v}')
#
#
# print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)

