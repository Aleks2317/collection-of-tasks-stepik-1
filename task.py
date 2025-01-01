# def count_calls():
#     def inner():
#         inner.total_calls += 1
#     inner.total_calls = 0
#     return inner
#
#
#
# counter = count_calls()
# counter()
# counter()
# print(counter.total_calls)
# counter()
# print(counter.total_calls)



# def some_other_function():
#     print("Теперь ты не просто функция!")
#
#
# def replace(f):
#     return some_other_function
#
#
# @replace
# def just_function():
#     print("Я просто функция")
#
# just_function()

# def multiply(arg: int | float):
#     print(arg)
#     def f_s(x: int | float):
#         print(f'arg внутри f_s {arg}')
#         print(f'x внутри f_s {x}')
#         return arg * x
#     return f_s
#
# f_2 = multiply(2)
# print(f'передали f_2')
# print("Умножение 2 на 5 =", f_2(5))
# print("Умножение 2 на 15 =", f_2(15))
#
# f_3 = multiply(3)
# print("Умножение 3 на 5 =", f_3(5))
# print("Умножение 3 на 15 =", f_3(15))
#
#
# def create_dict(key: int = 1):
#     res = {}
#     def c_d(x):
#         nonlocal key, res
#         res[key] = x
#         key += 1
#         return res
#     return c_d
#
#
# f_1 = create_dict()
# print(f_1('privet'))f
# print(f_1('poka'))
# print(f_1([5, 2, 3]))
#
# f2 = create_dict()
# print(f2(5))
# print(f2(15))

def add_args(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner

