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
    time: O(n*(n/k))
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
        for i in range(len(m)):
            print(m[i])
        text = encode(sentence, m)
    print(f"Result:\n'{text}'\n")


# sentence = "A quick brown fox jumps over the lazy dog"
# cipher(sentence)
sentence = "Hell"
cipher(sentence, 5)
# cipher(sentence, 1)
# cipher(sentence, 0)
