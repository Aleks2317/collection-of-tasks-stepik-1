def print_scores(name: str, *args) -> None:
    print(name)
    for grade in sorted(args):
        print(grade)


print_scores("Jud", 100, 95, 88, 92, 99)