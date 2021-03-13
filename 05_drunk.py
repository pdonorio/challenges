"""
>>> decode(5)
'Input is not a string'
>>> decode('yvvi')
'beer'
>>> decode('Blf zoivzwb szw 10 yvvih')
'You already had 10 beers'
>>> decode("Ovg'h hdrn rm gsv ulfmgzrm!")
"Let's swim in the fountain!"
>>> decode("Tl slnv, blf'iv wifmp")
"Go home, you're drunk"
"""


def decode(string_: str) -> str:
    if not isinstance(string_, str):
        return 'Input is not a string'

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reverse_alphabet = alphabet[::-1]
    alphabet += alphabet.upper()
    reverse_alphabet += reverse_alphabet.upper()
    mapping = {char: reverse_alphabet[index] for index, char in enumerate(alphabet)}

    string = ""
    for char in string_:
        if char in alphabet:
            char = mapping[char]
        string += char
    return string


# import string
# def decode(sentence):
#     table = str.maketrans(
#         string.ascii_lowercase +
#         string.ascii_uppercase,
#         string.ascii_lowercase[::-1] +
#         string.ascii_uppercase[::-1]
#     )
#     if isinstance(sentence, str):
#         return str.translate(sentence, table)
#     else:
#         return 'Input is not a string'


if __name__ == '__main__':
    import doctest

    doctest.testmod()
