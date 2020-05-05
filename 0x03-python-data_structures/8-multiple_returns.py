#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if len(sentence) == 0:
        alpha = None
    else:
        alpha = sentence[0]
    return size, alpha
