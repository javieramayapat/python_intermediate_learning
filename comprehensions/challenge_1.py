def run():
    # 🎯 SChallenge 1: Create a list comprehension, containing all multiples of 4
    # that are also multiples of 6 and 9, up to 5 digits.

    # Solution 1
    squares = [number for number in range(
        1, 99999)
        if number % 4 == 0 if number % 6 == 0 if number % 9 == 0]
    # print(squares)


if __name__ == '__main__':
    run()
