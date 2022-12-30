# Probelm Description
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

# Output Examples
"""
Input: s = "anagram", t = "nagaram"
Output: true
Input: s = "rat", t = "car"
Output: false
"""

# Problem Solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        return s == t
