# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

# Example 2:
# Input: nums = [7,7], k = 1
# Output: [7]

from typing import List
from collections import Counter

class Solution:
    def topKfrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq_counter = []

        for num, freq in counter.items():
            freq_counter[freq].append(num)
        
        result = []
        
        for i in range(len(freq_counter) - 1, -1, -1):
            for num in freq_counter[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result

test = Solution()
print(test.topKfrequent([1,2,2,3,3,3], 2))
print(test.topKfrequent([7,7], 1))