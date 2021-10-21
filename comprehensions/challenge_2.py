import numpy as np


def run():
    # 🎯 Create a dictionary that contains like key the first 1000 numbers
    # the values  its square root

    dictionary = {number: np.sqrt(number)
                  for number in range(1, 100)}
    print(dictionary)


if __name__ == '__main__':
    run()
