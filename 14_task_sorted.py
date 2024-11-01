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

def print_results(marks:list[tuple]) -> None:
    [print(*mark) for mark in sorted(marks, key=lambda x: (x[1], x[0].lower()), reverse=True)]



marks = [('English', 88), ('Science', 90), ('Maths', 88),
         ('Physics', 93), ('History', 78), ('French', 78),
         ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
print_results(marks)
