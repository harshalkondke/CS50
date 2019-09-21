from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""

    aLine = set(a.split("\n"))
    bLine = set(b.split("\n"))

    return aLine & bLine

def sentences(a, b):
    """Return sentences in both a and b"""

    asent = set(sent_tokenize(a))
    bsent = set(sent_tokenize(b))

    return asent & bsent

def substring_token(str, n):
    substring = []

    for i in range(len(str) - n +1):
        substring.append(str[i:i+n])

    return substring

def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    asub = set(substring_token(a, n))
    bsub = set(substring_token(b, n))

    return asub & bsub