def run():
    """
    Challenge: Return only even numbers from a list -> [1,2,3,4,5,6,7,8,9,10]
    """
    # solution with list comprehension
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = [number for number in numbers if number % 2 == 0]
    print(result)

    # solution with filter
    solution = list(filter(lambda number: number % 2 == 0,numbers))
    print(solution)


if __name__ == '__main__':
    run()
