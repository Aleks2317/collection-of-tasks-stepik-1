'''
Функция «Калькулятор»
Пользуясь вложенными функциями, реализуйте простой калькулятор. Для этого необходимо реализовать функцию calculate , которая принимает три параметра:

обязательный числовой параметр x
обязательный числовой параметр y
необязательный строковый параметр operation,  по умолчанию принимает значение английской буквы a
В данной функции должны быть реализованы следующие функции:

addition - сложение двух чисел,
subtraction - вычитание из первого переданного параметра второго;
division - деление первого на второго,
multiplication - умножение двух чисел.
Каждая из этих четырёх вложенных функций должна распечатать результат математической операции и ничего не возвращать

А при помощи параметра operation и условного оператора нужно выбрать какая из функций должна быть вызвана:

если operation = a, вызываем функцию addition;
если operation = s, вызываем функцию subtraction;
если operation = d, вызываем функцию division;
если operation = m, вызываем функцию multiplication;
calculate(2, 5) # Печатает 7.0
calculate(2.2, 15, 'a') # Печатает 17.2
calculate(22, 15, 's') # Печатает 7.0
calculate(2, 3.2, 'm') # Печатает 6.4
calculate(10, 0.4, 'd') # Печатает 25.0


Если operation принимает значение, отличное от перечисленных выше букв, то необходимо вывести на экран  сообщение «Ошибка. Данной операции не существует».

Также если мы выполняем деление, то второе число (y) не должно равняться нулю, в противном случае необходимо вывести на экран: «На ноль делить нельзя!».

Вам необходимо написать только определение функции  calculate

Sample Input 1:

calculate(10, 4, 's')
Sample Output 1:

6
Sample Input 2:

calculate(10, 0, 'd')
Sample Output 2:

На ноль делить нельзя!
Sample Input 3:

calculate(10, 4, 'w')
Sample Output 3:

Ошибка. Данной операции не существует
Sample Input 4:

calculate(1, 2, 'a')
Sample Output 4:

3
Sample Input 5:

calculate(3, 1, 'd')
Sample Output 5:

3.0
'''


def calculate(x: int | float, y: int | float, operation='a') -> callable:
    '''простой калькулятор'''

    def addition(x: int | float, y: int | float) -> int | float:
        '''сложение двух чисел'''
        print(x + y)

    def subtraction(x: int | float, y: int | float) -> int | float:
        '''вычитание из первого переданного параметра второго'''
        print(x - y)

    def division(x: int | float, y: int | float) -> int | float:
        '''деление первого на второго'''
        print(x / y if y > 0 else 'На ноль делить нельзя!')

    def multiplication(x: int | float, y: int | float) -> int | float:
        '''умножение двух чисел'''
        print(x * y)

    if operation in ('a', 's', 'd', 'm'):
        {'a': addition, 's': subtraction, 'd': division, 'm': multiplication}.get(operation)(x, y)
    else:
        print('Ошибка. Данной операции не существует')


calculate(10, 4, 's')

'''
def calculate(x: int | float, y: int | float, operation: str = 'a') -> None:

    def addition(a: int | float, b: int | float) -> None:
        print(a + b)

    def subtraction(a: int | float, b: int | float) -> None:
        print(a - b)

    def multiplication(a: int | float, b: int | float) -> None:
        print(a * b)

    def division(a: int | float, b: int | float) -> None:
        if b == 0:
            print('На ноль делить нельзя!')
        else:
            print(a / b)

    match operation:
        case 'a':
            addition(x, y)
        case 's':
            subtraction(x, y)
        case 'd':
            division(x, y)
        case 'm':
            multiplication(x, y)
        case _:
            print('Ошибка. Данной операции не существует')
'''
