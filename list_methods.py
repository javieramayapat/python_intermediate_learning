def run():

    # Append() -> Add a item at the end of the list
    number_list = [1, 2, 3, 4, 5, 6]
    number_list.append(7)
    print(number_list)

    # clear() -> empty all elements in a list
    list_to_clean = ['JS', 'PHP', 'Python', 'C', 'C++']
    list_to_clean.clear()
    print(list_to_clean)

    # extend() -> join one list to another one
    list1 = ['Hola', 'me']
    list2 = ['llamo','Javier']
    list1.extend(list2)


if __name__ == '__main__':
    run()
