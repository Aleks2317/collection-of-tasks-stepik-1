# def print_scores(name: str, *args) -> None:
#     print(name)
#     for grade in sorted(args):
#         print(grade)
#
#
# print_scores("Jud", 100, 95, 88, 92, 99)

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