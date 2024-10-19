'''Автоматизируем ресторан: вакантные столы
К нам обратились работники одного известного ресторана с просьбой написать приложение, которое позволяет автоматизировать процесс резервации столов. Одним из этапов процесса является определение свободных столов, чтобы затем можно было их предложить забронировать клиентам.

Всего в ресторане имеется 9 столиков. Информация о брони хранится в глобальной переменной tables в словаре следующего формата

tables = {
  1: 'Andrey',
  2: None,
  3: None,
  4: None,
  5: None,
  6: None,
  7: None,
  8: None,
  9: None,
}
Ключи здесь - номера столов, значения - имена клиентов, если бронь имеется, иначе None.

По текущему состоянию бронирования видно, что только столик под номером 1 занят Андреем, все остальные столики свободны. Значение None является признаком того, что столик никем не занят.

Ваша задача написать две функции, которые помогут определять какие столы сейчас свободны:

    ✔  функцию is_table_free, которая принимает номер стола и возвращает ответ на вопрос: «Свободен ли данный стол?» в виде булева значения

    ✔ функцию get_free_tables, которая вернет список всех свободных столов.'''


#
# def is_table_free(table: int) -> bool:
#     global tables
#     return tables.get(table) == None
#
# def get_free_tables():
#     return [table for table, name in tables.items() if name == None]

# tables = {
#   1: 'Andrey',
#   2: None,
#   3: 'Gena',
#   4: None,
#   5: 'Vasiliy',
#   6: 'Chubaka',
#   7: None,
#   8: 'Stas',
#   9: None,
# }
#
# print(is_table_free(5))
# print(is_table_free(6))
# print(get_free_tables())

"""  ✔  функцию reserve_table, которая принимает номер стола и имя клиента, 
проверяет свободен ли указанный столик и если за ним никто не прикреплен, 
вносятся данные клиента. Больше данная функция ничего не делает.
 Для реализации этой функции можете воспользоваться функцией is_table_free из задания «Автоматизируем ресторан: вакантные столы»

    ✔ функцию delete_reservation, которая очищает запись о бронировании.

Sample Input 1:

tables = {
    1: 'Andrey',
    2: None,
    3: 'Gena',
    4: 'Artem',
    5: 'Vasiliy',
    6: None,
    7: 'Artur',
    8: None,
    9: 'Misha',
}
print(tables)
delete_reservation(1)
delete_reservation(3)
reserve_table(6, 'Chubaka')
print(tables)
Sample Output 1:

{1: 'Andrey', 2: None, 3: 'Gena', 4: 'Artem', 5: 'Vasiliy', 6: None, 7: 'Artur', 8: None, 9: 'Misha'}
{1: None, 2: None, 3: None, 4: 'Artem', 5: 'Vasiliy', 6: 'Chubaka', 7: 'Artur', 8: None, 9: 'Misha'}"""

# def is_table_free(table: int) -> bool:
#     global tables
#     return tables.get(table) == None
#
# # def get_free_tables():
# #     return [table for table, name in tables.items() if name == None]
#
# def reserve_table(number_table: int, name: str) -> None :
#     global tables
#     if is_table_free(number_table) == False:
#         tables[number_table] = name
#
# def delete_reservation(number_table: str) -> None:
#     global tables
#     tables[number_table] = None


"""Резервация столов: изменение требований
Через некоторое время менеджеры ресторана поняли, что помимо имени клиента, 
они бы еще хотели хранить его принадлежность к статусу VIP клиента. Соответственно, 
они бы хотели изменить структуру хранения резерваций на следующую:

tables = {
    1: {'name': 'Andrey', 'is_vip': True},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False},
    6: None,
    7: None,
    8: None,
    9: None,
}
Здесь мы видим, что информация о клиенте хранится во вложенном словаре, у которого имеются два ключа name и is_vip.

Исходя из новой структуры данных, ваша задача теперь сделать рефакторинг кода функции reserve_table. 
Теперь она должна принимать не два аргумента, а три: номер стола, имя клиента и статус VIP. 
Делать проверку свободен ли стол и если она пройдена, сохранять данные в описанной выше структуре



Для успешного прохождения тестов скопируйте также реализацию функции delete_reservation 
 из задания «Резервация столов» и все ее зависимости от других функций, если они были

Sample Input 1:

tables = {
    1: {'name': 'Andrey', 'is_vip': True},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False},
    6: None,
    7: None,
    8: None,
    9: None,
}

print(tables)
reserve_table(3, 'Gena', True)
reserve_table(4, 'Artem', False)
reserve_table(5, 'Artur', True)  # Артур не должен занять место Василия
print(tables)"""

def is_table_free(number_table: int) -> bool:
    global tables
    return tables.get(number_table) != None


def get_free_tables():
    return [table for table, name in tables.items() if name == None]


def reserve_table(number_table: int, name: str, status_vip=False) -> None :
    global tables
    if is_table_free(number_table) == False:
        print(3)
        print(is_table_free(3))
        tables[number_table] = {'name': name, 'is_vip': status_vip}


def delete_reservation(number_table: str) -> None:
    global tables
    tables[number_table] = None

tables = {
    1: {'name': 'Andrey', 'is_vip': True},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False},
    6: None,
    7: None,
    8: None,
    9: None,
}

print({1: {'name': 'Andrey', 'is_vip': True}, 2: None, 3: None, 4: None, 5: {'name': 'Vasiliy', 'is_vip': False},
       6: None, 7: None, 8: None, 9: None}, {1: {'name': 'Andrey', 'is_vip': True}, 2: None,
                                             3: {'name': 'Gena', 'is_vip': True},
                                             4: {'name': 'Artem','is_vip': False},
                                             5: {'name': 'Vasiliy', 'is_vip': False},
                                             6: None, 7: None, 8: None, 9: None}, sep='\n')
print(tables)
reserve_table(3, 'Gena', True)
reserve_table(4, 'Artem', False)
reserve_table(5, 'Artur', True)  # Артур не должен занять место Василия
print(tables)