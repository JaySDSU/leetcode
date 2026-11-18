# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Example 2:
# Input: strs = ["x"]
# Output: [["x"]]
from typing import List

class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        anagram_groups = {}
        
        for word in words:
            freq_counter = [0] * 26
            for char in word:
                freq_counter[ord(char) - ord('a')] += 1
            key = tuple(freq_counter)
            if key not in anagram_groups:
                anagram_groups[key] = word
            else:
                anagram_groups[key].append(word)
        
        return list(anagram_groups.values())

test = Solution()
print(test.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(test.groupAnagrams(["x"]))

