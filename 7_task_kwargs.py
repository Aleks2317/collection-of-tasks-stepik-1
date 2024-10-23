'''Напишите функцию info_kwargs, которая принимает произвольное количество именованных аргументов.

Функция info_kwargs должна распечатать именованные аргументы (каждый на новой строке) в виде пар «ключ = значение», где ключи должны следовать в алфавитном порядке.

Вам необходимо написать только определение функции info_kwargs

Sample Input 1:

info_kwargs(first_name="John", last_name="Doe", age=33)
Sample Output 1:

age = 33
first_name = John
last_name = Doe
Sample Input 2:

info_kwargs(c=43, b= 32, a=32)'''


def info_kwargs(**kwargs: dict) -> None:

    [print(f'{key} = {kwargs[key]}') for key in sorted(kwargs.keys())]


info_kwargs(c=43, b= 32, a=32)
