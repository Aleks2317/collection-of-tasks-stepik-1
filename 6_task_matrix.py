'''Ваша задача — создать функцию create_matrix, которая имеет следующие параметры:

необязательный числовой параметр size - размер квадратной матрицы, по умолчанию принимает значение 3;

необязательный числовой параметр up_fill - значение заполнителя элементов, находящихся выше главной диагонали.
По умолчанию равен 0;

необязательный числовой параметр down_fill - значение заполнителя элементов, находящихся ниже главной диагонали.
По умолчанию равен 0.
Функция create_matrix должна возвращать квадратную матрицу размером size х size,
на диагонали которой располагаются числа от 1 до size. Все остальные элементы
заполнены согласно параметрам up_fill и down_fill.

Ваша задача написать только определение функции create_matrix'''


# def create_matrix(size=3, up_fill=0, down_fill=0) -> list:
#     matrix = [[0] * size for _ in range(size)]
#     for i in range(size):
#         for j in range(size):
#             if i == j:
#                 matrix[i][j] = (i + 1)
#             elif i < j:
#                 matrix[i][j] = up_fill
#             else:
#                 matrix[i][j] = down_fill
#     return matrix

def create_matrix(size=3, up_fill=0, down_fill=0) -> list:
    matrix = [[i + 1 if i == j else 0 for j in range(size)] for i in range(size)]

    if up_fill != 0 or down_fill != 0:
        for i in range(size):
            for j in range(size):
                if i == j:
                    continue
                matrix[i][j] = up_fill if i < j else down_fill

    return matrix


print(create_matrix())
print(create_matrix(up_fill=7))
