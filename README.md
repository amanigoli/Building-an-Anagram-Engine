# Building-an-Anagram-Engine
In this assignment you are tasked with building an anagram engine. An anagram is a word in which the exact letters of a word can be reordered to make a seperate word. 

For example the word glare can have its letters reordered to make large or lager or the word evil can be reordered to make veil or live.
Your engine is expected to store lists for these anagrams. As you will be using a key value pair database it is recommended that to generate keys you reorder the letters of a word in lexicographical order. The value should be a list of words that contains the exact letters (and quantities) of the key.

A user should be able to store these lists independently as they may be using different dictionaries for different tasks. The should be able to look for sub-anagrams as well. A sub-anagram is a smaller collection of letters taken from the original anagram to produce smaller words. e.g. for glare, sub-anagrams might be ael to produce ale and aegr to produce rage.
