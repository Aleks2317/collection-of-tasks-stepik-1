'''
Обменный пункт
Одной из базовых банковских услуг является обмен валют.

Напишите функцию convert, которая умеет конвертировать доллар в другую валюту и наоборот. Для конвертации используются текущие курсы валют, которые хранятся в глобальном словаре exchange_rates.

Результат округлите до двух знаков после запятой при помощи функции round

Sample Input 1:

currency = convert("USD", "EUR", 100)
print(currency)
Sample Output 1:

86.18
Sample Input 2:

currency = convert("USD", "AUD", 1000)
print(currency)
Sample Output 2:

1333.68
Sample Input 3:

currency = convert("EUR", "USD", 100)
print(currency)
Sample Output 3:

116.04
Sample Input 4:

currency = convert("GBP", "USD", 100)
print(currency)
Sample Output 4:

137.6
'''

exchange_rates = {
    "USD": 1.0,
    "EUR": 0.861775,
    "GBP": 0.726763,
    "INR": 75.054725,
    "AUD": 1.333679,
    "CAD": 1.237816,
    "SGD": 1.346851,
}

def convert(val1: str, val2:str, count: int) -> float:
    return round(count * (exchange_rates[val2] / exchange_rates[val1] ), 2)


currency = convert("EUR", "USD", 100)
print(currency)


currency = convert("GBP", "USD", 100)
print(currency)

