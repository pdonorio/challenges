"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

>>> pig_it('Pig latin is cool')
'igPay atinlay siay oolcay'
>>> pig_it('This is my string')
'hisTay siay ymay tringsay'
"""


def algo(word: str) -> str:
    if not word.isalpha():
        return word
    return word[1:] + word[0] + 'ay'


def pig_it(text: str) -> str:
    return " ".join(map(algo, text.split()))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
