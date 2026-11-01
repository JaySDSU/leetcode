# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# Two strings are anagrams if they contain the same characters, with each character appearing the same number of times, regardless of order.


# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"
# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_counter = [0] * 26
        
        for char in range(len(s)):
            freq_counter[ord(s[char]) - ord('a')] += 1
            freq_counter[ord(t[char]) - ord('a')] -= 1
        
        for count in freq_counter:
            if count != 0:
                return False
        return True

test = Solution()
print(test.isAnagram("racecar", "carrace"))
print(test.isAnagram("jar", "jam"))