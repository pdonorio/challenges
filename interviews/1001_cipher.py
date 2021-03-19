"""
- Given a string "s" implement the routing cipher on the string and return a new string. https://inventwithpython.com/hacking/chapter8.html
"""


def build_matrix(sentence: str, key: int) -> list:
    """
    n: len(sentence)
    time: O(n)
    space: O(n)
    """
    m = []
    while len(sentence) > key:
        m.append(sentence[:key])
        sentence = sentence[key:]
    m.append(sentence)
    return m


def encode(sentence: str, m: list) -> str:
    """
    n: len(sentence)
    k: cipher key
    time: O(n + n/k) = O(n)
    space: O(n)
    """
    text = ""
    col = -1
    sentence_len = len(sentence)
    while len(text) < sentence_len:
        col += 1
        for i in range(len(m)):
            if len(m[i]) > col:
                text += m[i][col]
    return text


def cipher(sentence: str, key: int = 10) -> str:
    print(f"Input: key {key}\n'{sentence}'")
    if key < 2 or key >= len(sentence):
        text = sentence
    else:
        m = build_matrix(sentence, key)
        # for i in range(len(m)):
        #     print(m[i])
        text = encode(sentence, m)
    print(f"Result:\n'{text}'\n")


"""
A second updated version

def cipher(sentence, size, filling_char='*'):
    sentence_len = len(sentence)
    if size < 2 or size > sentence_len:
        return sentence

    # add as many chars as needed to be multiple of the size
    mod_res = sentence_len % size
    if mod_res > 0:
        sentence += ''.join([filling_char] * (size - mod_res))
    matrix = [sentence[i : i + size] for i in range(0, len(sentence), size)]
    # print(matrix)

    # now the zip function can transpose all chars, being a squared matrix
    # NOTE: we remove the filling chars before adding the row to the cipher
    return ''.join(''.join(arr).rstrip(filling_char) for arr in zip(*matrix))
"""


sentence = "A quick brown fox jumps over the lazy do"
print(cipher(sentence, 5))
sentence = "A quick brown fox jumps over the lazy dog"
cipher(sentence)
cipher(sentence, 8)
sentence = "Hell"
cipher(sentence, 5)
cipher(sentence, 1)
cipher(sentence, 0)
