# def replace(text: str, old: str, new=None) -> str:
#     if new is None:
#         new = ''
#     # return text.replace(old,new)
#     # return new.join(text.split(old))
#     return ''.join([new if a == old else a for a in text])
#
# print(replace('Нет', 'т'))
# print(replace('Bella Ciao', 'a'))
# print(replace('nobody; i myself farewell analysis', 'l', 'z'))


# def product(lst_numbers: list, start=1) -> int:
#     for i in lst_numbers:
#         start *= i
#     return start

#
# def add_item(product: str, quantity=1) -> None:
#     global shopping_list
#     shopping_list[product] = shopping_list.setdefault(product, 0) + quantity


"""Напишите функцию show_list, которая выводит список товаров из корзины (глобальная переменная shopping_list).
У функции show_list есть необязательный логический параметр include_quantities, по умолчанию принимает значение True.

Если include_quantities имеет значение True, вы должны выводить имя товара и его количество в следующем формате:

{количество}x{имя_товара},

иначе необходимо вывести только имя.

Напишите только реализацию функции show_list"""

def show_list(include_quantities=True) -> None:
    global shopping_list
    if include_quantities == True:
        [print(f'{value}x{key}') for key, value in shopping_list.items()]
    else:
        [print(key) for key in shopping_list.keys()]

shopping_list = {'Bread': 13, 'Potato': 5, 'Milk': 2, 'Orange': 5}
show_list(include_quantities=False)