"""Программе на вход поступают слова, разделенные пробелом. Ваша задача - проверить,
во всех ли словах есть английская буква A вне зависимости от регистра.
В качестве ответа программа должна вывести True или False."""

def xx(w):
    print(w)
    return 'A' in w.upper()


print(list(map(xx, input().split())))

