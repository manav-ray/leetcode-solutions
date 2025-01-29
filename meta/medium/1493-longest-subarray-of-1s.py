"""

Sliding window -> r increments by one and updates zero counter
In same loop, while there are more than 1 zeros, start "removing" elements from the left
by increment l pointer and decrementing zeros when applies

keep track of largest subarray (r-l)

Time complexity - O(n)
Space complexity - O(1)

"""


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        
        l = 0
        z = 0

        for r, num in enumerate(nums):
            if num == 0:
                z += 1
            
            while z > 1 and l < r:
                if nums[l] == 0:
                    z -= 1
                l += 1
            
            res = max(res, r - l)
        
        return res