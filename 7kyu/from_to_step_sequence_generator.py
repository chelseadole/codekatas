# https://www.codewars.com/kata/from-to-step-sequence-generator/python

def generator (From, To, Step):
    if not Step:
        return []
    if From < To:
        return [i for i in range(From, To + 1, Step)]
    return [i for i in range(From, To - 1, -Step)]


