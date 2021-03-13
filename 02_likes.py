"""
>>> likes([])
'no one likes this'
>>> likes(["Peter"])
'Peter likes this'
>>> likes(["Jacob", "Alex"])
'Jacob and Alex like this'
>>> likes(["Max", "John", "Mark"])
'Max, John and Mark like this'
>>> likes(["Alex", "Jacob", "Mark", "Max"])
'Alex, Jacob and 2 others like this'
"""


def likes(names: list) -> str:
    third_person = ''
    and_string = ""
    names_string = 'no one'

    num = len(names)
    if num < 2:
        third_person = 's'

    if num > 0:
        names_string = names[0]
        if num == 2:
            and_string = f"and {names[1]} "
        elif num > 2:
            names_string += f", {names[1]}"
            if num == 3:
                and_string = f"and {names[2]} "
            elif num > 3:
                and_string = f"and {num - 2} others "

    return f"{names_string} {and_string}like{third_person} this"


# https://www.codewars.com/kata/reviews/564425cc55d0e45b8c000087/groups/564ab1bc633fa1f3310000cb
# def likes(names: list) -> str:
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this',
#         2: '{} and {} like this',
#         3: '{}, {} and {} like this',
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
