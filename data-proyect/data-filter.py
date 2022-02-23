DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    # Crear filtro donde obtengo todos los nombres de los programadores que dominan Python
    all_python_devs = [employee['name']
                       for employee in DATA
                       if employee['language'] == 'python']

    # Crea un filtro para traer a todos los programadores de Platzi
    all_platzi_employees = [platzi_employee['name']
                            for platzi_employee in DATA if platzi_employee['organization'] == 'Platzi']

    # create a filter to get all people who age is equal or bigeer to 18
    adults = list(filter(lambda worker: worker['age'] >= 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))

    # Crear un nuevo diciconario que contenga una nueva llave old cuyo valor sea true si la persona es mayor o igual a 70 años
    # y false si es menor que 70 (Suma de diccionarios usando |)

    old_people = list(map(lambda employee: employee | {
                      'old': employee['age'] >= 70}, DATA))

    # --------------------- Challenge --------------------------- #

    # filter to get all programmer names which use Python using a combination with filter and Map
    python_devs = list(
        filter(lambda worker: worker['language'] == 'python', DATA))
    python_devs = list(map(lambda worker: worker['name'], python_devs))

    # Create a list of people who work with Platzi
    platzi_workers = list(
        filter(lambda worker: worker['organization'] == 'Platzi', DATA))

    platzi_workers = list(
        map(lambda worker: worker['name'], platzi_workers))

    # ------------- Challenges ------------ #

    # create a list of people´s name who age is equal or bigger to 18
    adults_name = [worker['name'] for worker in DATA if worker['age'] >= 18]
    print(adults_name)

    # Create a new dictionary containing a new key old whose value is true if the person is greater than or equal to 70 years old
    # and false if it is less than 70 (Sum of dictionaries using |)
    old_people_2 = [worker | {'old':  worker['age'] >= 70} for worker in DATA]
    print(old_people_2)


if __name__ == '__main__':
    run()
