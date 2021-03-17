"""
>>> order("is2 Thi1s T4est 3a")
'Thi1s is2 3a T4est'
>>> order("4of Fo1r pe6ople g3ood th5e the2")
'Fo1r the2 g3ood 4of th5e pe6ople'
>>> order("")
''
"""
import re

PATTERN = re.compile(r"[^0-9]+")


def order(sentence: str, sep: str = " ") -> str:
    d = {PATTERN.sub("", word): word for word in sentence.split(sep)}
    print(d)
    return sep.join([d[key] for key in sorted(d)])

    # NOTE: this solution is very cool
    # it sorts each word, putting this way the number at the beginning
    # https://www.codewars.com/kata/reviews/55c4624d0538cef0df00009c/groups/55c48715d2609d9b4b0000a6
    # return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

    # or ' '.join(sorted(sentence.split(), key=lambda w: re.sub(r"[^0-9]+", "", w)))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
