'''

Напишите функцию print_results, которая принимает список кортежей. Каждый элемент вложенного кортежа состоит из названия предмета и оценки по нему.

Функция print_results должна вывести информацию по экзаменам, отсортированную по возрастанию оценок. Название каждой пары предмета и оценки печатается на отдельной строке через пробел.

В случае равенства оценок предметы должны выводиться на экран в том же порядке, в котором они следовали во входном списке

Sample Input 1:

marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93), ('History', 82)]
print_results(marks)
Sample Output 1:

History 82
English 88
Science 90
Physics 93
Maths 97
Sample Input 2:

marks = [('English', 88), ('Science', 100), ('Maths', 81),
         ('Physics', 100), ('History', 82), ('Music', 100)]
print_results(marks)
Sample Output 2:

Maths 81
History 82
English 88
Science 100
Physics 100
Music 100
'''
from collections import Counter

# def print_results(aray:list[tuple]) -> None:
#     [print(*mark) for mark in sorted(aray, key=lambda x: x[1])]


'''
Результаты экзаменов - 2
Перепишите функцию print_results так, чтобы информация выводилась по убыванию оценок.

В случае равенства оценок предметы должны выводиться на экран в том же порядке, в котором они следовали во входном списке
'''

# def print_results(aray:list[tuple]) -> None:
#     [print(*mark) for mark in sorted(aray, key=lambda x: x[1], reverse=True)]
#

"""
Результаты экзаменов - 3
Перепишите функцию print_results так, чтобы информация выводилась по убыванию оценок, а в случае их равенства предметы должны выводиться в алфавитном порядке без учета регистра
"""
# def sort_marks(marks: tuple[str, int]) -> tuple:
#     return marks[1], marks[0].lower()

# def print_results(marks:list[tuple]) -> None:
#     [print(*mark) for mark in sorted(marks, key=lambda x: (-x[1], x[0].lower()))]


"""*******"""
# def print_results(lst: list[tuple[str, int], ...]) -> None:
#     for item, grade in sorted(lst, key=lambda x: (-x[1], x[0].lower())):
#         print(item, grade)



# marks = [('English', 88), ('Science', 90), ('Maths', 88),
#          ('Physics', 93), ('History', 78), ('French', 78),
#          ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
# print_results(marks)

'''
Результаты экзаменов - 4
Перепишите функцию print_results так, чтобы информация выводилась по убыванию оценок, а в случае их равенства
 предметы должны выводиться в обратном алфавитном порядке без учета регистра
'''

# def print_results(marks:list[tuple]) -> None:
#     [print(*mark) for mark in sorted(marks, key=lambda x: (x[1], x[0].lower()), reverse=True)]
#
#
#
# marks = [('English', 88), ('Science', 90), ('Maths', 88),
#          ('Physics', 93), ('History', 78), ('French', 78),
#          ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
# print_results(marks)


'''
Сортировка отрезков
Напишите функцию get_sort_lines, которая принимает список кортежей, в котором хранится информация о координатах двух точек на координатной прямой. Функция get_sort_lines должна вернуть новый список, в котором элементы расположены в порядке возрастания расстояния между точками, хранящимися в одном элементе.



В случае равенства расстояний необходимо сортировать по возрастанию значения координаты первой точки, затем по возрастанию значения второй точки

Sample Input 1:

lines = [(-4, 4), (2, 3), (5, 9), (-1, -3) ]
print(get_sort_lines(lines))
Sample Output 1:

[(2, 3), (-1, -3), (5, 9), (-4, 4)]
Sample Input 2:

lines = [(5, 4), (2, 3), (1, 0), (-1, -2) ]
print(get_sort_lines(lines))
Sample Output 2:

[(-1, -2), (1, 0), (2, 3), (5, 4)]
Sample Input 3:

lines = [(5, 6), (5, 4), (1, 0), (0, -1), (1, 2), (2, 1)]
print(get_sort_lines(lines))
Sample Output 3:

[(0, -1), (1, 0), (1, 2), (2, 1), (5, 4), (5, 6)]
'''

# def args_for_sort_list(arg: tuple[int, int]) -> tuple[int, int, int]:
#     return max(arg) - min(arg), arg[0], arg[1]
#
#
# def get_sort_lines(aray: list[tuple[int,int]]) -> list[tuple[int,int]]:
#     return sorted(aray, key=args_for_sort_list)
#
# lines = [(-4, 4), (2, 3), (5, 9), (-1, -3) ]
# print(get_sort_lines(lines))
#
# lines = [(5, 4), (2, 3), (1, 0), (-1, -2) ]
# print(get_sort_lines(lines))

'''
Сортировка товаров
Напишите функцию print_goods, которая принимает список словарей. В самих словарях хранится информация о товарах: имя, модель и цвет. Задача функции print_goods вывести на экран информацию о товарах  в следующем формате

Производитель: <make>, модель: <model>, цвет: <color>
при этом товары должны быть отсортированы по цвету в лексикографическом порядке (по алфавиту) без учета регистра и по убыванию модели (второй критерий сортировки)

Sample Input 1:

models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
          {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
          {'make': 'Apple', 'model': 10, 'color': 'Silver'},
          {'make': 'Oppo', 'model': 9, 'color': 'Red'},
          {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
          {'make': 'Honor', 'model': 3, 'color': 'Black'}]
print_goods(models)
'''

# def print_goods(models: list[dict]) -> None:
#     for product in sorted(models, key=lambda p: (p.get('color').upper(), -p.get('model'))):
#         print(f"Производитель: {product['make']}, модель: {product['model']}, цвет: {product['color']}")
#
#
# models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#           {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#           {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
#           {'make': 'Apple', 'model': 10, 'color': 'Silver'},
#           {'make': 'Oppo', 'model': 9, 'color': 'Red'},
#           {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
#           {'make': 'Honor', 'model': 3, 'color': 'Black'}]
# print_goods(models)

"""Сортировка товаров - 2
Поставщик скидывает нашему заказчику информацию о товарах, а он хочет взглянуть на нее в отсортированном виде. Заказчик хочет видеть вывод, где вверху самые дорогие товары, внизу самые дешевые.

Вот только поставщик предоставляет данные в виде списка строк, где каждая строка хранит информацию о товаре в виде

Название_товара: цена_товара
Название товара отделено от цены знаком двоеточия :.

Ваша задача написать функцию print_goods , которая принимает список строк. Далее print_goods  должна выводить информацию о товарах, сортируя их сперва по цене, а затем по алфавиту без учета регистра. Вывод информации о каждом товаре делается в отдельной строке в следующем формате

Цена_товара - Название_товара
Цена должна выводиться с точностью до двух знаком после запятой

Sample Input 1:

data = [
    'Sony PlayStation 5: 46000',
    'Телевизор QLED Samsung QE65Q60TAU: 87090',
    'Смартфон Samsung Galaxy A11: 10000',
    'Планшет Samsung Galaxy Tab S6: 26600',
]

print_goods(data)
Sample Output 1:

87090.00 - Телевизор QLED Samsung QE65Q60TAU
46000.00 - Sony PlayStation 5
26600.00 - Планшет Samsung Galaxy Tab S6
10000.00 - Смартфон Samsung Galaxy A11
Sample Input 2:

data = [
    'Sony PlayStation 5: 46000.5',
    'Телевизор QLED Samsung QE65Q60TAU: 87090',
    'Samsung Galaxy s23: 46000.5',
    'siemens eq.6 plus s100: 46000.5',
    'Samsung Galaxy Tab S6: 46000.5',
]
print_goods(data)

"""
#
# def print_goods(products: list[str]) -> None:
#     products = [p.split(':') for p in products]
#     for product in sorted(products, key=lambda x: (-float(x[1].strip()), x[0].lower())):
#         print(f"{'%.2f' % float(product[1])} - {product[0]}")
#
#
# data = [
#     'Sony PlayStation 5: 46000',
#     'Телевизор QLED Samsung QE65Q60TAU: 87090',
#     'Смартфон Samsung Galaxy A11: 10000',
#     'Планшет Samsung Galaxy Tab S6: 26600',
# ]
#
# print_goods(data)


'''
Премия Оскар
Представьте, что мы с вами сами можем решать кому и сколько статуэток Оскара уйдет (Лео бы тогда давно купался в этих статуэтках).

Ваша задача написать функцию print_best_and_worst_laureate, которая находит информацию, 
кто из номинантов получил наибольшее и наименьшее количество статуэток. 
Функция print_best_and_worst_laureate принимает на вход словарь, где указана номинация и имя победителя в ней 
(название фильма или имя актера).
На основании этой информации функция print_best_and_worst_laureate должна в отдельных строках вывести лауреатов премии, 
набравших наибольшее и наименьшее количество статуэток и через запятую их количество. 

Sample Input 1:

laureates = {'За лучший фильм': 'Все везде и сразу',
             'За лучшую музыку к фильму': 'На Западном фронте без перемен',
             'За лучший звук': 'Топ Ган: Мэверик',
             'За лучшие визуальные эффекты': 'Аватар: Путь воды',
             'За лучший дизайн костюмов': 'Топ Ган: Мэверик',
             'За лучшую операторскую работу': 'На Западном фронте без перемен',
             'За лучший монтаж': 'Все везде и сразу',
             'За лучший оригинальный сценарий': 'Все везде и сразу',
             'За лучший фильм на иностранном языке': 'Все везде и сразу', }

print_best_and_worst_laureate(laureates)
Sample Output 1:

Все везде и сразу, 4
Аватар: Путь воды, 1
Sample Input 2:

laureates = {'За лучший фильм': 'Оппенгеймер',
             'За лучшую музыку к фильму': 'Оппенгеймер',
             'За лучший звук': 'Зона интересов',
             'За лучшие визуальные эффекты': 'Бедные-несчастные',
             'За лучший дизайн костюмов': 'Бедные-несчастные',
             'За лучшую операторскую работу': 'Бедные-несчастные',
             'За лучший монтаж': 'Оппенгеймер',
             'За лучший оригинальный сценарий': 'Оппенгеймер',
             'За лучший фильм на иностранном языке': 'Зона интересов'}

print_best_and_worst_laureate(laureates)
Sample Output 2:

Оппенгеймер, 4
Зона интересов, 2
'''
# from collections import Counter
#
#
# def print_best_and_worst_laureate(laureate: dict) -> None:
#     res = {}
#     for value in laureate.values():
#         res[value] = res.get(value, 0) + 1
#     best = max(res, key=lambda x: res[x])
#     worst = min(res, key=lambda x: res[x])
#     print(f"{best}, {res[best]}\n{worst}, {res[worst]}")
#     d = dict(Counter(list(laureate.values())))
#     print(d)
#
#
# laureates = {'За лучший фильм': 'Все везде и сразу',
#              'За лучшую музыку к фильму': 'На Западном фронте без перемен',
#              'За лучший звук': 'Топ Ган: Мэверик',
#              'За лучшие визуальные эффекты': 'Аватар: Путь воды',
#              'За лучший дизайн костюмов': 'Топ Ган: Мэверик',
#              'За лучшую операторскую работу': 'На Западном фронте без перемен',
#              'За лучший монтаж': 'Все везде и сразу',
#              'За лучший оригинальный сценарий': 'Все везде и сразу',
#              'За лучший фильм на иностранном языке': 'Все везде и сразу', }
#
# print_best_and_worst_laureate(laureates)


"""
Рейтинг таксистов
Руководитель таксопарка хочет увидеть отчет по всем таксистам, где нужно указать имя таксиста и его среднюю оценку. 
Информацию в отчете нужно расположить по убыванию средней оценки таксиста. 
Для этого вам нужно написать функцию print_order_rating, которая принимает на вход список кортежей. 
Каждый кортеж состоит из двух элементов: имя таксиста и оценка за поездку (целое число от 1 до 5).

Функция print_order_rating должна расположить таксистов в порядке убывания их средней оценки 
и вывести имя каждого таксиста и его среднюю оценку в отдельной строке. 
В случае совпадения средних оценок нужно расположить каждую группу таксистов, имеющих одинаковый рейтинг,  
по имени в алфавитном порядке без учета регистра
"""

# def print_order_rating(order: list[tuple[str, int]]) -> None:
#     rating = {}
#     for k, v in order:
#         rating[k] = rating.setdefault(k, [0, 0])
#         rating[k][0] += v
#         rating[k][1] += 1
#     rating = {k: v[0] / v[1] for k, v in rating.items()}
#     for name in sorted(rating, key=lambda x: (-rating[x], x.upper())):
#         print(name, rating[name])

"""******
def print_order_rating(data: list[tuple[str, int], ...]) -> None:
    d = {}
    for name, rating in drivers:
        d.setdefault(name, []).append(rating)
    for name in sorted(d, key=lambda x: (-sum(d[x]) / len(d[x]), x.lower())):
        print(f'{name} {sum(d[name]) / len(d[name])}')
"""


# drivers = [
#     ('Зина', 5),
#     ('Зина', 3),
#     ('Гермиона', 4),
#     ('Гермиона', 4),
#     ('александр', 4),
# ]
# print_order_rating(drivers)



