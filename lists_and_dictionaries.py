def run():
    my_list = ['hola', True, 25, 12.5]
    dictionary = {"firstname": "Javier", "lastname": "Amaya"}

    list_of_dictionaries = [
        {"firstname": "Pablo", "lastname": "Trinidad"},
        {"firstname": "Jose", "lastname": "Torres"},
        {"firstname": "Toño", "lastname": "Lopez"},
        {"firstname": "Arturo", "lastname": "Perez"},
        {"firstname": "Maria", "lastname": "Delgado"},
    ]

    dictionary_of_lists = {
        "foods": ["enchiladas", "Tacos", "Mole", "Salpicón"],
        "Activities": ["Run", "Swim", "Listeng music", "walk in the park"],
        "lenguages": ["English", "Spanish", "French", "Italian"]
    }

    # Use a loop for to print key and value of the dictionary
    for key, value in dictionary_of_lists.items():
        # print(key, '-' ,value)
        pass
        
    #Print the values of the list_of_dictionaries
    for list in list_of_dictionaries:
        print(list)

if __name__ == '__main__':
    run()
