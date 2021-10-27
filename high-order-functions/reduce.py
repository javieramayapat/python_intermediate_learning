from functools import reduce


def run():
    """
    resuce this list [2,2,2,2,2] to 32
    in this case we only have to create a cumulative number
    """
    numbers = [2, 2, 2, 2, 2]
    solution = reduce(
        lambda number,
        next_number: number *
        next_number, numbers
    )
    print(solution)


if __name__ == '__main__':
    run()
