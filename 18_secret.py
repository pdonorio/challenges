"""
>>> triplets = [ ['t','u','p'], ['w','h','i'], ['t','s','u'], ['a','t','s'], ['h','a','p'], ['t','i','s'], ['w','h','s'] ]
>>> recoverSecret(triplets)
'whatisup'

"""


"""
def find_leftmost(triplets):
    # from itertools import chain
    # return set(chain(*triplets))
    return set(triplet[0] for triplet in triplets if len(triplet) > 0)


def is_on_right(triplets, candidate):
    for triplet in triplets:
        for index in [1, 2]:
            if len(triplet) > index and triplet[index] == candidate:
                return True
    return False


def remove_char(triplets, char):
    for i in range(len(triplets)):
        triplet = triplets[i]
        if len(triplet) > 0 and char == triplet[0]:
            triplet.pop(0)
    return triplets


def recoverSecret(triplets):

    # NOTE: zip can transpose a matrix
    # clever step from https://www.codewars.com/kata/reviews/53fbcb9ecfc5f67703000032/groups/565abdc360706fe46e000072
    # out = list(zip(*triplets))
    # print(set(out[0]) - set(out[1] + out[2]))

    secret = ""
    while sum(map(len, triplets)) > 0:
        for candidate in find_leftmost(triplets):
            if not is_on_right(triplets, candidate):
                secret += candidate
                break
        triplets = remove_char(triplets, candidate)
        # print(candidate, secret, triplets)
        # break
    return secret
"""


def recoverSecret(a):
    out = list(zip(*a))
    h = list(set(out[0]) - set(out[1] + out[2]))
    for i in a:
        if i[0] in h:
            i[:2], i[2] = i[1:], ''

    return h[0] + recoverSecret(a) if h else str()


if __name__ == '__main__':
    import doctest

    doctest.testmod()
