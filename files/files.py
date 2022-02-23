def read():
    """Function to read file´s number and add to a list
    """
    numbers = []
    with open('../documents/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    
    print(numbers)


def write():
    names = ['Javier','Marypaz','Daniela','Elvia','Jafet','Mariana','Luisa','Felipe']
    with open('../documents/names.txt','w', encoding='utf-8') as f:
    # with open('../documents/names.txt','w', encoding='utf-8') as f: Modo de escritura sin sobre escritura
        for name in names:
            f.write(name)
            f.write('\n')


def run():
    # read()
    write()


if __name__ == '__main__':
    run()
