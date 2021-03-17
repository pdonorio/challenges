"""
>>> find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ])
'BbBb'
>>> find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ])
'foo'
>>> find_uniq([ '    ', 'a', '  ' ])
'a'
"""


def find_uniq(arr: list) -> str:
    mappings = {}
    for string in arr:
        x = "".join(sorted(set(string.replace(' ', '').lower())))
        if x not in mappings:
            mappings[x] = string, False
        else:
            mappings[x] = string, True
            # can I break in here?

    for _, (string, duplicate) in mappings.items():
        if not duplicate:
            return string


if __name__ == '__main__':
    import doctest

    doctest.testmod()
