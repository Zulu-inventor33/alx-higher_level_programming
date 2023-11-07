#!/usr/bin/python3
def multiple_returns(sentence):
    """Return de length of a string and first char."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
