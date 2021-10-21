def run():
    # Create a dictionary that contains like key the first 100 numbers
    # the values the first 100 numbers cubed
    # only save number that aren´t divisible by 3
    
    dictionary = {i:i**3 for i in range(1, 100) if i%3 != 0}
    print(dictionary)


if __name__ == '__main__':
    run()
