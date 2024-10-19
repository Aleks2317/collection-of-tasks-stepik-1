"""Люди постоянно тратят время на игры, результат которых зависит только от удачи.
Подумать только, по доброй воле спускать деньги в казино! Мы, роботы, гораздо практичнее.
Давай сыграем в следующую игру. Я загадал
4
4 различных положительных целых числа A, B, C, D, при этом A < B < C < D. Я называю
8
8 чисел в произвольном порядке:
!  !
A, B, C, D
A × B  !
B × C
C × D  !
D × A

. Твоя задача — найти число D.
Справишься или предпочтешь игру попроще? Могу принести футбольный мячик. ⚽

Задание нужно выполнить в виде программы, которая получает на вход числа A, B, C, D, A × B, B × C, C × D, D × A
(на одной строке) согласно условию. Программа должна вывести одно число D."""

numbers = list(sorted(map(int, input().split())))

res = numbers.copy()
d_res = {}
A = numbers[0]  # min
B = numbers[1]
AB = A * B
CD = numbers[-1]

res.remove(A)
res.remove(B)
res.remove(AB)
res.remove(CD)
C = min(res)
print(res)
D = int(CD / min(res))

d_res['A'] = A
d_res['B'] = B
d_res['C'] = C
d_res['D'] = D
d_res['AB'] = AB
d_res['BC'] = B * min(res)
d_res['CD'] = CD
d_res['DA'] = A * D
print(D)
print(numbers)
print(d_res)

# def number_d(input_numbers: list) -> int:
#     cd = max(input_numbers)
#     if len(input_numbers) == 4:
#         return cd / min(input_numbers)
#     x =

# 2 3 4 1 12 6 2 4
# 2 6 7 3 14 35 15 5
# 1971 78 7644 98 27 5694 73 2646
