# Probelm Description
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

# Output Examples
"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

# Problem Solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        initialize a dict with default values of list
        map all lowercase english letters to a list of 0's
        for each word creat a count and put a 1 in place of any letter that appears in the word
        use that count as a key in the dict and append the word to that key's list 
        '''
        res = collections.defaultdict(list)
        for i in strs:
            count = [0] * 26
            for x in i:
                count[ord(x) - ord('a')] += 1
            res[tuple(count)].append(i)
        return res.values()
