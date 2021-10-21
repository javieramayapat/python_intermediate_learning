def run():
    # Get the first one hundred numbers to square
    square_number = [number ** 2 for number in range(1, 101) if number % 3 != 0]
    print(square_number)


if __name__ == '__main__':
    run()
