def get_divisors(number: int) -> list:

    # we only accept positive numbers
    assert number >= 1, f'{number} Only positive numbers are allowed'
    return [i for i in range(0, number + 1) if i % 2 == 0]


def run():
    try:
        number = int(input('Enter a number to calculate all divisors: '))
        print(get_divisors(number))
        print('End of the program')
    except ValueError:
        print('You must enter only numbers')


if __name__ == '__main__':
    run()
