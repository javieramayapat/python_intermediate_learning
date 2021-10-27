def run():
    """
    Create a new list with squared number of this list [1,2,3,4,5]
    """

    # Solution with listcomprehencion
    numbers = [1, 2, 3, 4, 5]
    result = [i**2 for i in numbers]
    print(result)

    # solucion with map
    solution = list(map(lambda number: number**2, numbers))
    print(solution)


if __name__ == '__main__':
    run()
