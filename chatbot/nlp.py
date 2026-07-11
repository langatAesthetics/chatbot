import string

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()


def tokenize(sentence: str) -> list:
    sentence = sentence.lower()

    translator = str.maketrans(
        "",
        "",
        string.punctuation
    )

    sentence = sentence.translate(
        translator
    )

    tokens = sentence.split()

    return tokens


def stem(word: str) -> str:
    """
    Reduce a word to its root form.
    """

    return stemmer.stem(word)

def stem_tokens(tokens):
    return [
        stem(token)
        for token in tokens
    ]
