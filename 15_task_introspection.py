'''
В python любое значение является объектом, и мы можем исследовать эти объекты. Сам язык предоставляет нам несколько встроенных функций и модулей, которые нам помогут в анализе объекта во время выполнения программы, а именно:

    ✔️ функция dir - встроенная функция, которая принимая объект в качестве аргумента и возвращает список допустимых атрибутов и методов для этого объекта.

    ✔️ объект type

    ✔️ функция isinstance

    ✔️ функция id

    ✔️ модуль inspect
'''

# my_list = [1, 2, 3]
# print(dir(my_list))

'''Напишите функцию get_info_about_object, которая принимает объект и выводит информацию обо всех его атрибутах и методах в следующем формате:

сперва выводится список всех атрибутов и методов
на следующей строке фраза «Всего у объекта {count} атрибутов и методов»


Примечание: тестирование на платформе будет производиться на версии Python 3.10, поэтому не переживайте, если вы используете у себя на устройстве другую версию python и у вас не совпадает вывод. 

Sample Input 1:

def print_goods(lst):
    pass

get_info_about_object(print_goods)'''


# def get_info_about_object(ob: object) -> None:
#     info_about_object = dir(ob)
#     print(info_about_object, f"Всего у объекта {len(info_about_object)} атрибутов и методов", sep='\n')
#
#
# def print_goods(lst):
#     pass
#
# get_info_about_object(print_goods)



# def check_exist_attrs(obj: object, atr: list[str]) -> dict[str, bool]:
#     atr_method_object = dir(obj)
#     return {k: True if k in atr_method_object else False for k in atr}

"""********
def check_exist_attrs(obj: object, attr_names: list[str, ...]) -> dict[str, bool]:
    return {attr_name: hasattr(obj, attr_name) for attr_name in attr_names}
"""
# def check_exist_attrs(obj: object, atr: list[str]) -> dict[str, bool]:
#     atr_method_object = dir(obj)
#     return {k: True if k in atr_method_object else False for k in atr}
#
#
# def create_attrs(obj: object, list_atr: list[tuple[str, int]]) -> None:
#     return [setattr(obj, k, v) for k, v in list_atr]
#
# def print_goods(lst):
#     pass
#
# print_goods.is_working = False
# print_goods.status = 'Not ready'
#
# print(check_exist_attrs(print_goods, ['is_working', 'status', 'time', 'speed']))


"""
Ваша задача написать функцию find_keys, которая принимает произвольное количество именованных аргументов. Функция должна отобрать только те имена параметров, у которых значения являются списками или кортежами. Функция find_keys должна собрать все имена таких параметров в список, отсортировать их по алфавиту вне зависимости от регистра букв и вернуть в качестве результата.

Ниже представлены примеры:

find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]) => ['A', 'b', 't', 'W']

find_keys(name='Bruce', surname='Wayne') => []

find_keys(marks=[4, 5], name='ashle', surname='Brown', age=20, Also=(1, 2)) => ['Also', 'marks']
Ваша задача написать только определение функции find_keys
"""

# def find_keys(**qwargs) -> list:
#     args = [k for k, v in qwargs.items() if isinstance(v, (list, tuple))]
#     return sorted(args, key=str.lower)
#
# print(find_keys(marks=[4, 5], name='Ashle', surname='Brown', age=20, Also=(1, 2)))


