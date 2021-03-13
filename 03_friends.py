"""
>>> friends(['Ryan', 'Kieran', 'Jason', 'Yous'])
['Ryan', 'Yous']

>>> friends(['Luigi', 'Mark', 'Paolo', 'Luca'])
['Mark', 'Luca']
"""


def friends(persons: list) -> list:
    return [person for person in persons if len(person) == 4]


# def friend(x):
#     return filter(lambda name: len(name) == 4, x)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
