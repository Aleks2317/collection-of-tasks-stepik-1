'''Напишите функцию rotate , которая имеет следующие параметры

    ✔️  lst - список чисел (целых или вещественных)

    ✔️  shift - целое число, обозначающее сдвиг. По умолчанию равен 1

Функция rotate должна выполнить циклический сдвиг элементов списка на shift позиций и вернуть
в качестве ответа новый список со смещенными значениями. Если значение shift положительно, сдвиг необходимо производить вправо, если отрицательно — влево.

На картинке ниже показан результат циклического сдвига элементов списка на единицу влево (источник картинки)'''

# def rotate(lst: list[int | float], shift: int = 1) -> list[int | float]:
#     '''Функция выполняет циклический сдвиг списка на shift позиций вправо(shift>0) или влево(shift<0)'''
#     shift = shift % len(lst) if abs(shift) > len(lst) else shift
#     if shift > 0:
#         return lst[-shift: ] + lst[:-shift]
#     return lst[shift:] + lst[:shift]



# 2
# def rotate(lst: list[int | float], shift: int = 1) -> list[int | float]:
#     '''Функция выполняет циклический сдвиг списка на shift позиций вправо(shift>0) или влево(shift<0)'''
#     shift = shift % len(lst) if abs(shift) > len(lst) else shift
#     return lst[-shift: ] + lst[:-shift]



nums = [1, 2, 3, 4]
new_nums = rotate(nums)
print(nums)
print(new_nums)
print()
print(rotate.__doc__)
print(rotate.__annotations__)
print(rotate([1, 2, 3, 4, 5, 6], 0))
print()
print(rotate([1, 2, 3, 4, 5, 6], -3))
print()
print(rotate([1, 2, 3, 4, 5, 6], -10))
print()
print(rotate([1, 2, 3, 4, 5, 6, 7], 21))


