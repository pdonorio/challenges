"""
>>> history = ["(555) 010-3535 00:13:24", "(442) 130-5165 01:36:26", "(333) 010-5135 01:38:24"]
>>> closest_friends(history)
['Jack', 'Melissa', 'John']
"""

import re
from datetime import datetime

phonebook = {
    'John': '(555) 010-3535',
    'Melissa': '(442) 130-5165',
    'Jack': '(333) 010-5135',
}
inverse_phonebook = {v: k for k, v in phonebook.items()}


def closest_friends(history: list) -> list:
    pattern = re.compile(r"^(\(\d+\) \d{3}\-\d{4}) (\d{2}\:\d{2}:\d{2})$")
    data = {}
    for element in history:
        number, duration = pattern.search(element).groups()
        name = inverse_phonebook[number]
        dt = datetime.strptime(duration, '%H:%M:%S')
        data[name] = dt
    sorted_data = sorted(data.items(), key=lambda item: item[1], reverse=True)
    return [name for (name, value) in sorted_data]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
