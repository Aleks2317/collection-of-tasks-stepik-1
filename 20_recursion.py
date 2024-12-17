def print_to(n: int) -> None:
    if n > 0:
        print_to(n - 1)
        print(n)

print_to(4)

