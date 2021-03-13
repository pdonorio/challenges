"""
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test
"""


def spin_words(sentence, min_len=5):
    return " ".join(
        word if len(word) < min_len else word[::-1] for word in sentence.split()
    )


x = spin_words("Hey fellow warriors")
print(x)
