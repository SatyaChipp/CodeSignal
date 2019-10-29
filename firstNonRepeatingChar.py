"""
Given a string s consisting of small English letters, find and return the first instance of a 
non-repeating character in it. If there is no such character, return '_'.
Example
For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.
There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.
For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.
There are no characters in this string that do not repeat.
"""

def firstNotRepeatingCharacter(s):
    from collections import Counter, OrderedDict
    loopin = OrderedDict()
    for i in s:
        loopin[i] = 1 if i not in loopin else loopin[i]+1
    for key, val in loopin.items():
        if val==1:
            return key
    return '_'
    

