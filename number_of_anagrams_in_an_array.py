"""
An anagram is a word, a phrase, or a sentence formed from another by rearranging its letters. An example of this is "angel", which is an anagram of "glean".

Write a function that receives an array of words, and returns the total number of distinct pairs of anagramic words inside it.

Some examples:

There are 2 anagrams in the array ["dell", "ledl", "abc", "cba"]
There are 7 anagrams in the array ["dell", "ledl", "abc", "cba", "bca", "bac"]

https://www.codewars.com/kata/number-of-anagrams-in-an-array-of-words/python
"""


def _are_anagrams(word1, word2):
    """Check if word1 and word2 are anagrams."""
    return sorted(list(word1)) == sorted(list(word2))


def anagram_counter(words):
    anagrams = []

    for x in range(len(words)):
        for i in range(len(words)):
            if x == i:
                continue
            elif _are_anagrams(words[i], words[x]):
                anagrams.append(sorted([words[i], words[x]]))
    return len(anagrams) / 2



