"""
Функция-применитель
Напишите функцию apply, которая принимает функцию и итерируемый объект (например, список) и применяет функцию к каждому элементу итерируемого объекта.

В качестве ответа функция apply должна вернуть список из вычисленных значений.

Sample Input 1:

def square(num):
    return num ** 2

print(apply(square, [5, 7, 0, 3]))
"""

# def apply(func, args) -> list:
#     return [func(i) for i in args]


"""
Множественное вычисление
Затем создайте функцию compute, которая принимает список функций и произвольное количество значений. Функция compute 
должна применить каждую функцию к каждому значению в переданном порядке и сформировать из полученных значений новый 
список, который и будет возвращаться в качестве ответа
"""

def compute(lst: list[callable], *args) -> list:
    return [f(i) for f in lst for i in args]



def square(num):
    return num ** 2

def inc(num):
    return num + 1

def dec(num):
    return num - 1

print(compute([inc, dec, square], 10, 20, 30, 40))